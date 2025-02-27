from django.shortcuts import render  # type: ignore
from django.views.generic.detail import DetailView  # type: ignore
from .models import Book, Library  # ✅ Now importing both Book and Library

# Function-Based View: List All Books


def list_books(request):
    books = Book.objects.all()  # ✅ Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Library Details


class LibraryDetailView(DetailView):
    model = Library  # ✅ Specifies the model
    template_name = 'relationship_app/library_detail.html'  # ✅ Uses the correct template
    context_object_name = 'library'