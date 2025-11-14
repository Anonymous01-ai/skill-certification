# Skill Certification Web App

A complete end-to-end testing and certification platform built with React and Flask. Users can sign up, take profession-specific MCQ tests, and receive digital certificates upon passing.

## 🚀 Features

- **User Authentication**: JWT-based auth with email/password + simulated Google login
- **Role-Based Testing**: Tests for Cleaner, Plumber, Electrician, and Carpenter
- **Random Question Selection**: 10 random questions from a pool of 20 per test
- **Payment Simulation**: Mock payment system with admin discount
- **Multiple Attempts**: Up to 3 attempts per certification
- **Digital Certificates**: Instant PDF certificate generation and download
- **Admin Features**: Special pricing (Rs. 500 vs Rs. 800)
- **Responsive Design**: Beautiful UI with TailwindCSS

## 📁 Project Structure

```
project/
├── backend/
│   ├── app.py                 # Flask application
│   ├── models.py              # Database models
│   ├── config.py              # Configuration
│   ├── seed_questions.py      # Database seeding script
│   ├── requirements.txt       # Python dependencies
│   └── routes/
│       ├── auth.py           # Authentication routes
│       ├── test.py           # Test routes
│       └── certificate.py    # Certificate routes
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── components/       # Reusable components
    │   ├── context/          # Auth context
    │   ├── pages/            # Page components
    │   ├── utils/            # API utilities
    │   ├── App.jsx
    │   └── index.jsx
    ├── package.json
    └── tailwind.config.js
```

## 🛠️ Tech Stack

### Backend
- **Flask**: Python web framework
- **PostgreSQL**: Database
- **SQLAlchemy**: ORM
- **Flask-JWT-Extended**: JWT authentication
- **ReportLab**: PDF generation
- **bcrypt**: Password hashing
- **Alembic**: Database migrations

### Frontend
- **React 18**: UI library
- **React Router**: Navigation
- **TailwindCSS**: Styling
- **Axios**: HTTP client
- **Context API**: State management

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 12+
- npm or yarn

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
cd "Testing Website"
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env file with your database credentials
# DATABASE_URL=postgresql://username:password@localhost:5432/skill_certification
```

### 3. Database Setup

```bash
# Create PostgreSQL database
createdb skill_certification

# Or using psql
psql -U postgres
CREATE DATABASE skill_certification;
\q
```

### 4. Seed the Database

```bash
# Run the seeding script to populate questions
python seed_questions.py
```

This will:
- Create all database tables
- Insert 20 MCQ questions for Cleaner (and sample questions for other roles)
- Create an admin user

**Admin Credentials:**
- Email: `admin@skilltest.com`
- Password: `admin123`

### 5. Start Backend Server

```bash
python app.py
```

Backend will run on: `http://localhost:5001`

### 6. Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will run on: `http://localhost:3000`

## 🎯 Usage Guide

### User Journey

1. **Landing Page**: Browse categories, view information
2. **Sign Up**: Register with name, email, password, and profession
3. **Login**: Login with credentials or simulated Google login
4. **Home**: View dashboard with attempt status
5. **Payment**: Simulate payment (Rs. 800 for users, Rs. 500 for admin)
6. **Test**: Answer 10 random MCQ questions
7. **Results**: View score and pass/fail status
8. **Certificate**: Download PDF certificate if passed

### Test Rules

- **Passing Score**: 7 out of 10 correct answers
- **Attempts**: Maximum 3 attempts per user
- **Questions**: 10 random questions from a pool of 20
- **After 3rd Attempt**: Physical assistance message shown

### Admin Features

- Login with admin credentials for special pricing
- Automatic payment processing
- Discounted fee: Rs. 500 (vs Rs. 800 for regular users)

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/google-login` - Simulated Google login
- `GET /api/auth/me` - Get current user

### Test
- `GET /api/test/questions/<role>` - Get 10 random questions
- `POST /api/test/submit-test` - Submit test answers
- `GET /api/test/attempts` - Get user's attempts
- `GET /api/test/attempt-count` - Get attempt count

### Certificate
- `GET /api/certificate/<user_id>` - Get certificate data
- `GET /api/certificate/<user_id>/download` - Download PDF

## 📝 Adding More Questions

To add questions for other professions, edit `backend/seed_questions.py`:

```python
MCQ_DATA = {
    "Cleaner": [...],  # Already populated
    "Plumber": [...],  # Add 20 questions
    "Electrician": [...],  # Add 20 questions
    "Carpenter": [...]  # Add 20 questions
}
```

Then run:
```bash
python seed_questions.py
```

## 🎨 Customization

### Change Branding
- Update logo/name in `frontend/src/components/Navbar.jsx`
- Modify colors in `frontend/tailwind.config.js`

### Modify Test Rules
- Change passing score in `backend/routes/test.py`
- Update attempt limit in `backend/routes/test.py`

### Update Payment Fees
- Edit fees in `frontend/src/pages/Payment.jsx`

## 🐛 Troubleshooting

### Database Connection Error
```bash
# Check PostgreSQL is running
pg_ctl status

# Update DATABASE_URL in backend/.env
```

### Port Already in Use
```bash
# Backend (5000)
lsof -ti:5000 | xargs kill -9

# Frontend (3000)
lsof -ti:3000 | xargs kill -9
```

### CORS Errors
- Ensure Flask-CORS is installed
- Check frontend API URL in `src/utils/api.js`

## 📦 Production Deployment

### Backend (Heroku/Railway)
```bash
# Add Procfile
web: python app.py

# Set environment variables
DATABASE_URL=<production_db_url>
JWT_SECRET_KEY=<secure_random_key>
```

### Frontend (Netlify/Vercel)
```bash
# Build
npm run build

# Update API URL in production
REACT_APP_API_URL=<production_api_url>
```

## 🔒 Security Notes

- Change `JWT_SECRET_KEY` in production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Implement rate limiting for API endpoints
- Add CSRF protection

## 📄 License

This project is for educational purposes.

## 👥 Support

For issues or questions:
- Email: support@skillcert.com
- Phone: +92 300 1234567

## 🎉 Credits

Built with React, Flask, PostgreSQL, and TailwindCSS.

---

**Happy Coding! 🚀**
