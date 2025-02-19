# Delete the book
book.delete()

# Check if book still exists
books = Book.objects.all()
print(books)  # Expected output: <QuerySet []>
