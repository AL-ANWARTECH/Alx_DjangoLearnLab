from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from .serializers import BookSerializer
from .models import Book

# Create your views here.
# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer