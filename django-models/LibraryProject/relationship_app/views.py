from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Book, Library, UserProfile

# ====== Book and Library Views ======


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# ====== Authentication Views ======


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")  # Redirect to books list after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# ====== Role-Based Access Control ======


def has_role(user, role):
    """Check if the user has the given role."""
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == role


def role_required(role):
    """Decorator to enforce role-based access."""
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not has_role(request.user, role):
                messages.error(
                    request, f"You do not have permission to access the {role} dashboard.")
                return redirect("login")
            return view_func(request, *args, **kwargs)
        return login_required(wrapper, login_url="login")
    return decorator


@role_required("Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@role_required("Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@role_required("Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html")
