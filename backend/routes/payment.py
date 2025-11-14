from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, PaymentRecord, db

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/authorize-payment', methods=['POST'])
@jwt_required()
def authorize_payment():
    """Verify admin credentials before simulating payment."""
    data = request.get_json() or {}
    admin_email = data.get('admin_email')
    admin_password = data.get('admin_password')

    if not admin_email or not admin_password:
        return jsonify({'error': 'Admin email and password are required'}), 400

    admin = User.query.filter_by(email=admin_email, is_admin=True).first()

    if not admin or not admin.check_password(admin_password):
        return jsonify({'error': 'Invalid admin credentials'}), 401

    return jsonify({'authorized': True}), 200


@payment_bp.route('/record', methods=['POST'])
@jwt_required()
def record_payment():
    """Record a payment made by the authenticated user."""
    data = request.get_json() or {}
    amount = data.get('amount')
    discounted = data.get('discounted', False)

    if amount is None:
        return jsonify({'error': 'Payment amount is required'}), 400

    try:
        amount = int(amount)
    except (TypeError, ValueError):
        return jsonify({'error': 'Payment amount must be an integer value'}), 400

    if amount <= 0:
        return jsonify({'error': 'Payment amount must be greater than zero'}), 400

    try:
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        payment = PaymentRecord(
            user_id=user_id,
            amount=amount,
            discounted=bool(discounted)
        )

        db.session.add(payment)
        db.session.commit()

        return jsonify({'message': 'Payment recorded successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
