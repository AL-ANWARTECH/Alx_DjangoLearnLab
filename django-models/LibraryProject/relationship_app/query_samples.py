from relationship_app.models import Author, Book, Library, Librarian
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()


# Query all books by a specific author

def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return author.books.all()
    return []

# List all books in a library


def books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.books.all()
    return []

# Retrieve the librarian for a library


def librarian_of_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.librarian
    return None


if __name__ == "__main__":
    # Example Queries
    print("Books by Author 'John Doe':", books_by_author('John Doe'))
    print("Books in Library 'City Library':", books_in_library('City Library'))
    print("Librarian of 'City Library':", librarian_of_library('City Library'))
