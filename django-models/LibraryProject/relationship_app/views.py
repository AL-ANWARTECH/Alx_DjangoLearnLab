from django.shortcuts import render  # type: ignore
from django.views.generic import DetailView  # type: ignore
from .models import Book, Library
from .models import Library
from django.views.generic.detail import DetailView  # type: ignore

# Function-based view to list all books


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
