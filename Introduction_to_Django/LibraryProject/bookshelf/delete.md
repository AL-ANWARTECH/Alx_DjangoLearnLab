from bookshelf.models import Book
# Delete the book
book.delete()

# Check if book still exists
books = Book.objects.all()
print(books)  # Expected output: <QuerySet []>
