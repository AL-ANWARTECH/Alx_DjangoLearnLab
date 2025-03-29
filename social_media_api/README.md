# Social Media API

## Posts API Endpoints

- `GET /api/posts/`: List all posts (paginated)
- `POST /api/posts/`: Create a new post (authenticated)
- `GET /api/posts/<id>/`: Retrieve a specific post
- `PUT/PATCH /api/posts/<id>/`: Update a post (author only)
- `DELETE /api/posts/<id>/`: Delete a post (author only)
- `POST /api/posts/<id>/like/`: Like/unlike a post (authenticated)

- `GET /api/posts/<post_pk>/comments/`: List comments for a post
- `POST /api/posts/<post_pk>/comments/`: Create a comment on a post (authenticated)
- `GET /api/posts/<post_pk>/comments/<id>/`: Retrieve a specific comment
- `PUT/PATCH /api/posts/<post_pk>/comments/<id>/`: Update a comment (author only)
- `DELETE /api/posts/<post_pk>/comments/<id>/`: Delete a comment (author only)

### Example Requests

**Create a Post:**
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{"title": "My First Post", "content": "This is my first post content"}'
## Follow System API Endpoints

- `POST /api/auth/follow/<user_id>/`: Follow a user (authenticated)
- `POST /api/auth/unfollow/<user_id>/`: Unfollow a user (authenticated)
- `GET /api/auth/following/`: List users you're following (authenticated)
- `GET /api/auth/followers/`: List your followers (authenticated)

## Feed Endpoint

- `GET /api/feed/`: Get posts from users you follow (authenticated)
  - Ordered by most recent first
  - Includes your own posts

### Example Requests

**Follow a user:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/follow/2/ \
-H "Authorization: Bearer <your_token>"
## Likes API Endpoints

- `POST /api/posts/<post_id>/like/`: Like a post (authenticated)
- `POST /api/posts/<post_id>/unlike/`: Unlike a post (authenticated)

## Notifications API Endpoints

- `GET /api/notifications/`: List all notifications (authenticated)
- `POST /api/notifications/<notification_id>/read/`: Mark notification as read (authenticated)
- `POST /api/notifications/read-all/`: Mark all notifications as read (authenticated)

### Example Responses

**Like a post:**
```json
{
    "status": "Post liked",
    "likes_count": 5
}
