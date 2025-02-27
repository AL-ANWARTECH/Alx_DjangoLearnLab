from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views properly

urlpatterns = [
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register_view, name="register"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(),
         name="library_detail"),

    # Role-based access URLs
    path("admin-dashboard/", views.admin_view, name="admin_dashboard"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_dashboard"),
    path("member-dashboard/", views.member_view, name="member_dashboard"),
]
