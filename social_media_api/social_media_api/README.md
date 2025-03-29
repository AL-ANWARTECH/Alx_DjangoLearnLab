# Social Media API Documentation

## **Project Setup**
1. Install dependencies: `pip install django djangorestframework djangorestframework-authtoken`
2. Start Django project: `django-admin startproject social_media_api`
3. Create accounts app: `python manage.py startapp accounts`
4. Add `rest_framework`, `rest_framework.authtoken`, and `accounts` to `INSTALLED_APPS`
5. Set up the custom user model
6. Apply migrations: `python manage.py makemigrations && python manage.py migrate`
7. Run the server: `python manage.py runserver`

## **Features**
- User authentication (registration, login, token-based authentication)
- Create, read, update, and delete (CRUD) operations for posts and comments
- User follow/unfollow functionality
- User feed displaying posts from followed users
- Pagination for large datasets
- Filtering posts by title and content
- Secure API with permissions

---

## **API Endpoints**

### **User Authentication**

 Method  Endpoint                 Description              

 POST    `/api/auth/register/`     Register a new user      
 POST    `/api/auth/login/`        Log in and get a token   
 GET     `/api/auth/profile/`      View user profile        
 PATCH   `/api/auth/profile/`      Update profile          

---

### **Follow & Unfollow Users**
Users can follow or unfollow other users using the following endpoints.

#### **Follow a User**
- **Endpoint:** `POST /api/follow/<user_id>/`
- **Description:** Allows an authenticated user to follow another user.
- **Request Headers:**
  - `Authorization: Token <your_token>`
- **Response Example:**
```json
{
    "message": "You are now following johndoe"
}
```

#### **Unfollow a User**
- **Endpoint:** `POST /api/unfollow/<user_id>/`
- **Description:** Allows an authenticated user to unfollow a previously followed user.
- **Request Headers:**
  - `Authorization: Token <your_token>`
- **Response Example:**
```json
{
    "message": "You have unfollowed johndoe"
}
```

---

### **User Feed**
Users can view posts from people they follow.

#### **Get Feed**
- **Endpoint:** `GET /api/feed/`
- **Description:** Retrieves a feed of posts from users the authenticated user follows.
- **Request Headers:**
  - `Authorization: Token <your_token>`
- **Response Example:**
```json
[
    {
        "id": 1,
        "author": "johndoe",
        "title": "My First Post",
        "content": "This is a post from a followed user.",
        "created_at": "2025-03-29T10:30:00Z"
    },
    {
        "id": 2,
        "author": "janedoe",
        "title": "Another Post",
        "content": "Sharing my thoughts here.",
        "created_at": "2025-03-28T18:20:00Z"
    }
]
```

---

## **Testing Follow & Feed Features**

1. **Follow a user**
   - Send a `POST` request to `/api/follow/<user_id>/` with a valid authentication token.
   - Check if the response confirms the follow action.

2. **Unfollow a user**
   - Send a `POST` request to `/api/unfollow/<user_id>/` with a valid authentication token.
   - Verify that the response confirms the unfollow action.

3. **View Feed**
   - Send a `GET` request to `/api/feed/` with a valid authentication token.
   - Ensure that posts from followed users appear in the response.

4. **Edge Cases to Test**
   - Following a user that is already followed.
   - Unfollowing a user that is not being followed.
   - Viewing the feed when not following anyone.

---

## **Future Enhancements**
- Add JWT authentication
- Implement password reset
- Add user search & follow suggestions

