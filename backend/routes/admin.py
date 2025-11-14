from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from models import User, Attempt, PaymentRecord, db

admin_bp = Blueprint('admin', __name__)


def _require_admin(user_id):
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return None, jsonify({'error': 'Admin access required'}), 403
    return user, None, None


@admin_bp.route('/analytics', methods=['GET'])
@jwt_required()
def get_analytics():
    """Return platform analytics for admin dashboard."""
    user_id = int(get_jwt_identity())
    admin_user, error_response, status_code = _require_admin(user_id)
    if error_response:
        return error_response, status_code

    total_users = User.query.filter_by(is_admin=False).count()
    total_admins = User.query.filter_by(is_admin=True).count()

    total_attempts = Attempt.query.count()
    total_passed = Attempt.query.filter_by(passed=True).count()
    total_failed = total_attempts - total_passed

    revenue_total = db.session.query(func.coalesce(func.sum(PaymentRecord.amount), 0)).scalar() or 0
    discounted_payments = PaymentRecord.query.filter_by(discounted=True).count()
    regular_payments = PaymentRecord.query.filter_by(discounted=False).count()

    passes_by_category_query = (
        db.session.query(User.role, func.count(Attempt.id))
        .join(Attempt, Attempt.user_id == User.id)
        .filter(Attempt.passed.is_(True))
        .group_by(User.role)
    )
    passes_by_category = {role: count for role, count in passes_by_category_query.all()}

    recent_payments_query = (
        PaymentRecord.query.order_by(PaymentRecord.created_at.desc()).limit(5).all()
    )
    recent_payments = [
        {
            'id': payment.id,
            'user': payment.user.name if payment.user else 'Unknown',
            'amount': payment.amount,
            'discounted': payment.discounted,
            'created_at': payment.created_at.isoformat()
        }
        for payment in recent_payments_query
    ]

    return jsonify({
        'totals': {
            'users': total_users,
            'admins': total_admins,
            'tests_taken': total_attempts,
            'tests_passed': total_passed,
            'tests_failed': total_failed
        },
        'revenue': {
            'total_amount': revenue_total,
            'discounted_payments': discounted_payments,
            'regular_payments': regular_payments
        },
        'passes_by_category': passes_by_category,
        'recent_payments': recent_payments
    }), 200


@admin_bp.route('/users', methods=['GET'])
@jwt_required()
def list_users():
    """Return detailed information about all users."""
    user_id = int(get_jwt_identity())
    _, error_response, status_code = _require_admin(user_id)
    if error_response:
        return error_response, status_code

    users = User.query.order_by(User.created_at.desc()).all()

    data = []
    for user in users:
        attempts = user.attempts or []
        payments = user.payments or []

        attempts_total = len(attempts)
        attempts_passed = sum(1 for attempt in attempts if attempt.passed)
        attempts_failed = attempts_total - attempts_passed

        last_attempt = max((attempt.timestamp for attempt in attempts), default=None)
        last_payment = max((payment.created_at for payment in payments), default=None)

        payments_total_amount = sum(payment.amount for payment in payments)
        payments_count = len(payments)

        data.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role,
            'is_admin': user.is_admin,
            'created_at': user.created_at.isoformat() if user.created_at else None,
            'attempts_total': attempts_total,
            'attempts_passed': attempts_passed,
            'attempts_failed': attempts_failed,
            'last_attempt_at': last_attempt.isoformat() if last_attempt else None,
            'payments_total_amount': payments_total_amount,
            'payments_count': payments_count,
            'last_payment_at': last_payment.isoformat() if last_payment else None
        })

    return jsonify({'users': data}), 200


@admin_bp.route('/users/<int:target_user_id>', methods=['PUT'])
@jwt_required()
def update_user(target_user_id):
    """Update user details."""
    user_id = int(get_jwt_identity())
    _, error_response, status_code = _require_admin(user_id)
    if error_response:
        return error_response, status_code

    target_user = User.query.get(target_user_id)
    if not target_user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json() or {}
    allowed_fields = {'name', 'email', 'role', 'is_admin'}

    updates = {key: data[key] for key in allowed_fields if key in data}

    if not updates:
        return jsonify({'error': 'No valid fields provided for update'}), 400

    if 'email' in updates:
        email = updates['email']
        if not email:
            return jsonify({'error': 'Email cannot be empty'}), 400
        existing = User.query.filter(User.email == email, User.id != target_user_id).first()
        if existing:
            return jsonify({'error': 'Email already in use'}), 400
        target_user.email = email

    if 'name' in updates:
        name = updates['name']
        if not name:
            return jsonify({'error': 'Name cannot be empty'}), 400
        target_user.name = name

    if 'role' in updates:
        role = updates['role']
        if not role:
            return jsonify({'error': 'Role cannot be empty'}), 400
        target_user.role = role

    if 'is_admin' in updates:
        target_user.is_admin = bool(updates['is_admin'])

    try:
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Invalid data provided'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/users/<int:target_user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(target_user_id):
    """Delete a user and all related records."""
    user_id = int(get_jwt_identity())
    _, error_response, status_code = _require_admin(user_id)
    if error_response:
        return error_response, status_code

    if user_id == target_user_id:
        return jsonify({'error': 'You cannot delete your own account'}), 400

    target_user = User.query.get(target_user_id)
    if not target_user:
        return jsonify({'error': 'User not found'}), 404

    try:
        db.session.delete(target_user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
