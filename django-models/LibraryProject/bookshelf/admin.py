from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Columns in list view
    search_fields = ("title", "author") # Enables search bar
    list_filter = ("publication_year",) # Adds a filter for publication year
    
