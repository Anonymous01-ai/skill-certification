from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    attempts = db.relationship('Attempt', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hash password using bcrypt"""
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        """Verify password"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat()
        }

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)
    # Optional Urdu translations
    question_text_ur = db.Column(db.Text)
    option_a_ur = db.Column(db.String(255))
    option_b_ur = db.Column(db.String(255))
    option_c_ur = db.Column(db.String(255))
    option_d_ur = db.Column(db.String(255))
    
    def to_dict(self, include_answer=False, language='en'):
        language = (language or 'en').lower()

        def localized(primary, translated):
            if language == 'ur' and translated:
                return translated
            return primary

        data = {
            'id': self.id,
            'role': self.role,
            'question_text': localized(self.question_text, self.question_text_ur),
            'question_text_en': self.question_text,
            'question_text_ur': self.question_text_ur,
            'option_a': localized(self.option_a, self.option_a_ur),
            'option_a_en': self.option_a,
            'option_a_ur': self.option_a_ur,
            'option_b': localized(self.option_b, self.option_b_ur),
            'option_b_en': self.option_b,
            'option_b_ur': self.option_b_ur,
            'option_c': localized(self.option_c, self.option_c_ur),
            'option_c_en': self.option_c,
            'option_c_ur': self.option_c_ur,
            'option_d': localized(self.option_d, self.option_d_ur),
            'option_d_en': self.option_d,
            'option_d_ur': self.option_d_ur
        }
        if include_answer:
            data['correct_option'] = self.correct_option
        return data

class Attempt(db.Model):
    __tablename__ = 'attempts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    attempt_number = db.Column(db.Integer, nullable=False)
    passed = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'score': self.score,
            'attempt_number': self.attempt_number,
            'passed': self.passed,
            'timestamp': self.timestamp.isoformat()
        }


class PaymentRecord(db.Model):
    __tablename__ = 'payment_records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    discounted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('payments', lazy=True, cascade='all, delete-orphan'))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'discounted': self.discounted,
            'created_at': self.created_at.isoformat()
        }
