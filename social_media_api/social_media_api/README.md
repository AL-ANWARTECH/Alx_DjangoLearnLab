# Social Media API

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT tokens
- `GET /api/auth/profile/` - View/update user profile (authenticated)

## User Model
The custom user model includes:
- Standard Django user fields
- Bio (text field)
- Profile picture (image field)
- Followers (many-to-many relationship)