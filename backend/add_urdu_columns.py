"""
Migration script to add Urdu translation columns to questions table
Run this once to update the database schema
"""
from app import create_app
from models import db

def add_urdu_columns():
    app = create_app()
    
    with app.app_context():
        print('Adding Urdu translation columns to questions table...')
        
        # SQL to add new columns
        sql_commands = [
            "ALTER TABLE questions ADD COLUMN IF NOT EXISTS question_text_ur TEXT;",
            "ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_a_ur VARCHAR(255);",
            "ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_b_ur VARCHAR(255);",
            "ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_c_ur VARCHAR(255);",
            "ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_d_ur VARCHAR(255);"
        ]
        
        try:
            for sql in sql_commands:
                db.session.execute(db.text(sql))
            
            db.session.commit()
            print('✓ Successfully added Urdu translation columns')
            print('You can now run seed_questions.py to populate the database')
            
        except Exception as e:
            db.session.rollback()
            print(f'✗ Error adding columns: {str(e)}')
            raise

if __name__ == '__main__':
    add_urdu_columns()
