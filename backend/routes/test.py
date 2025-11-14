from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Question, Attempt, User
import random

from translation_utils import translate_text

test_bp = Blueprint('test', __name__)

@test_bp.route('/questions/<role>', methods=['GET'])
@jwt_required()
def get_questions(role):
    """Fetch 10 random questions for the specified role"""
    try:
        language = request.args.get('lang', 'en').lower()

        # Get all questions for this role
        all_questions = Question.query.filter_by(role=role).all()
        
        if len(all_questions) < 10:
            return jsonify({
                'error': f'Not enough questions available for {role}. Need at least 10.'
            }), 400
        
        # Select 10 random questions
        selected_questions = random.sample(all_questions, 10)

        translations_made = False

        if language == 'ur':
            fields = [
                ('question_text', 'question_text_ur'),
                ('option_a', 'option_a_ur'),
                ('option_b', 'option_b_ur'),
                ('option_c', 'option_c_ur'),
                ('option_d', 'option_d_ur')
            ]

            for question in selected_questions:
                for source_attr, target_attr in fields:
                    source_value = getattr(question, source_attr)
                    target_value = getattr(question, target_attr)

                    if source_value and not target_value:
                        translated = translate_text(source_value, dest='ur')
                        if translated:
                            setattr(question, target_attr, translated)
                            translations_made = True

            if translations_made:
                db.session.commit()

        # Return questions without correct answers
        questions_data = [
            q.to_dict(include_answer=False, language=language)
            for q in selected_questions
        ]
        
        return jsonify({
            'questions': questions_data,
            'language': language
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@test_bp.route('/submit-test', methods=['POST'])
@jwt_required()
def submit_test():
    """Evaluate test submission and save attempt"""
    try:
        user_id = int(get_jwt_identity())
        data = request.get_json()
        
        # Validate request
        if 'answers' not in data:
            return jsonify({'error': 'Answers are required'}), 400
        
        answers = data['answers']  # Format: {question_id: selected_option}
        
        # Get user
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # Count previous attempts
        previous_attempts = Attempt.query.filter_by(user_id=user_id).count()
        attempt_number = previous_attempts + 1
        
        # Calculate score
        score = 0
        total_questions = len(answers)
        
        for question_id, selected_option in answers.items():
            question = Question.query.get(int(question_id))
            if question and question.correct_option == selected_option:
                score += 1
        
        # Determine pass/fail
        passed = False
        message = ''
        
        if attempt_number <= 2:
            # First two attempts: normal evaluation
            if score >= 7:
                passed = True
                message = f'Congratulations! You passed with {score}/10'
            else:
                message = f'You scored {score}/10. You need at least 7 to pass. You have {3 - attempt_number} attempt(s) remaining.'
        elif attempt_number == 3:
            # Third attempt
            if score >= 7:
                passed = True
                message = f'Congratulations! You passed with {score}/10'
            else:
                message = f'You scored {score}/10. Physical assistance required for final verification.'
        else:
            # After 3rd attempt with physical assistance
            passed = True
            message = f'You have passed after physical verification with score {score}/10'
        
        # Save attempt
        attempt = Attempt(
            user_id=user_id,
            score=score,
            attempt_number=attempt_number,
            passed=passed
        )
        db.session.add(attempt)
        db.session.commit()
        
        return jsonify({
            'score': score,
            'total': total_questions,
            'passed': passed,
            'attempt_number': attempt_number,
            'message': message,
            'can_retry': attempt_number < 3 and not passed
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@test_bp.route('/attempts', methods=['GET'])
@jwt_required()
def get_attempts():
    """Get all attempts for current user"""
    try:
        user_id = int(get_jwt_identity())
        
        attempts = Attempt.query.filter_by(user_id=user_id).order_by(Attempt.timestamp.desc()).all()
        
        return jsonify({
            'attempts': [attempt.to_dict() for attempt in attempts]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@test_bp.route('/attempt-count', methods=['GET'])
@jwt_required()
def get_attempt_count():
    """Get attempt count for current user"""
    try:
        user_id = int(get_jwt_identity())
        
        count = Attempt.query.filter_by(user_id=user_id).count()
        passed_attempt = Attempt.query.filter_by(user_id=user_id, passed=True).first()
        
        return jsonify({
            'attempt_count': count,
            'has_passed': passed_attempt is not None
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@test_bp.route('/reset-attempts', methods=['POST'])
@jwt_required()
def reset_attempts():
    """Reset attempts for current user after repayment"""
    try:
        user_id = int(get_jwt_identity())

        total_attempts = Attempt.query.filter_by(user_id=user_id).count()
        passed_attempt = Attempt.query.filter_by(user_id=user_id, passed=True).first()

        if passed_attempt:
            return jsonify({'error': 'Cannot reset attempts after passing the test'}), 400

        if total_attempts < 3:
            return jsonify({'error': 'Repayment not required yet'}), 400

        Attempt.query.filter_by(user_id=user_id).delete(synchronize_session=False)
        db.session.commit()

        return jsonify({'message': 'Attempts reset successfully', 'attempt_count': 0}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
