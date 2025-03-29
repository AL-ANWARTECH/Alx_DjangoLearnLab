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

