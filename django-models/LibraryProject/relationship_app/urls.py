from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    register_view, list_books, LibraryDetailView,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)

urlpatterns = [
    # Authentication URLs
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register_view, name="register"),

    # Book and Library URLs
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Book Management URLs (Protected by Permissions)
    path("books/add/", add_book, name="add_book"),
    path("books/edit/<int:book_id>/", edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", delete_book, name="delete_book"),

    # Role-based Access URLs
    path("admin-dashboard/", admin_view, name="admin_dashboard"),
    path("librarian-dashboard/", librarian_view, name="librarian_dashboard"),
    path("member-dashboard/", member_view, name="member_dashboard"),
]
