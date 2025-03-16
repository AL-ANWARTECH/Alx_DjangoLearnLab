## API Endpoints

### Books

- **GET /api/books/**: List all books.
- **GET /api/books/<int:pk>/**: Retrieve a single book by ID.
- **POST /api/books/create/**: Create a new book (requires authentication).
- **PUT /api/books/<int:pk>/update/**: Update an existing book (requires authentication).
- **DELETE /api/books/<int:pk>/delete/**: Delete a book (requires authentication).

### Permissions

- Read-only endpoints (`GET`) are accessible to all users.
- Write endpoints (`POST`, `PUT`, `DELETE`) require authentication.
