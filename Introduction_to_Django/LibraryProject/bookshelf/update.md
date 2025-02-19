# Update book title
book.title = "Nineteen Eighty-Four"
book.save()

# Retrieve updated book
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)  # Expected output: Nineteen Eighty-Four
