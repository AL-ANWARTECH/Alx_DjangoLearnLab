# Social Media API

## **Project Setup**
1. Install dependencies: `pip install django djangorestframework djangorestframework-authtoken`
2. Start Django project: `django-admin startproject social_media_api`
3. Create accounts app: `python manage.py startapp accounts`
4. Add `rest_framework`, `rest_framework.authtoken`, and `accounts` to `INSTALLED_APPS`
5. Set up the custom user model
6. Apply migrations: `python manage.py makemigrations && python manage.py migrate`
7. Run the server: `python manage.py runserver`

## **API Endpoints**
 Method  Endpoint         Description 
 POST    `/api/auth/register/`  Register a new user 
 POST    `/api/auth/login/`  Log in and get a token 
 GET     `/api/auth/profile/`  View user profile 
 PATCH   `/api/auth/profile/`  Update profile 

## **Testing**
- Use **Postman** or **cURL** to test API calls.

## **Future Enhancements**
- Add JWT authentication
- Implement password reset
- Add user search & follow feature
# Social Media API

This is a RESTful API built with Django and Django REST Framework that allows users to create, view, update, and delete posts and comments.

## Features
- User authentication (registration, login, token-based authentication)
- Create, read, update, and delete (CRUD) operations for posts and comments
- Pagination for large datasets
- Filtering posts by title and content
- Secure API with permissions