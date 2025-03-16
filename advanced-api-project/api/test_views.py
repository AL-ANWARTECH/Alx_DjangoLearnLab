from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create initial data for testing
        self.book1 = Book.objects.create(
            title="1984",
            author="George Orwell",
            publication_year=1949
        )
        self.book2 = Book.objects.create(
            title="Animal Farm",
            author="George Orwell",
            publication_year=1945
        )

    def test_create_book(self):
        """
        Ensure we can create a new book.
        """
        url = reverse('book-list')
        data = {
            'title': 'Brave New World',
            'author': 'Aldous Huxley',
            'publication_year': 1932
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=3).title, 'Brave New World')

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a book.
        """
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    def test_update_book(self):
        """
        Ensure we can update a book.
        """
        url = reverse('book-detail', args=[self.book1.id])
        data = {
            'title': '1984',
            'author': 'George Orwell',
            'publication_year': 1950  # Update publication year
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book1.id).publication_year, 1950)

    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """
        Ensure we can filter books by author.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'author': 'George Orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books are by George Orwell

    def test_search_books(self):
        """
        Ensure we can search books by title.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Animal'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')

    def test_order_books(self):
        """
        Ensure we can order books by publication year.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')  # Published in 1945
        self.assertEqual(response.data[1]['title'], '1984')  # Published in 1949