from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
import os
from dotenv import load_dotenv

# Load environment variables from .env before importing configuration
load_dotenv()

from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    jwt = JWTManager(app)
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.test import test_bp
    from routes.certificate import certificate_bp
    from routes.payment import payment_bp
    from routes.admin import admin_bp
    from routes.translate import translate_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(test_bp, url_prefix='/api/test')
    app.register_blueprint(certificate_bp, url_prefix='/api')
    app.register_blueprint(payment_bp, url_prefix='/api/payment')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(translate_bp, url_prefix='/api')
    
    # Health check endpoint
    @app.route('/')
    def index():
        return jsonify({
            'message': 'Skill Certification API',
            'status': 'running'
        })
    
    @app.route('/api/health')
    def health():
        return jsonify({'status': 'healthy'}), 200
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
