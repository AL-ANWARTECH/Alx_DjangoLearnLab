from relationship_app.models import Author, Book, Library, Librarian
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


# Query all books by a specific author

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)  # ✅ Fixed
    except Author.DoesNotExist:
        return []

# List all books in a library


def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library


def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Sample usage
if __name__ == "__main__":
    print("Books by Author X:", books_by_author("Author X"))
    print("Books in Library Y:", books_in_library("Library Y"))
    print("Librarian of Library Y:", librarian_of_library("Library Y"))
