# import_books.py
import json
from django.core.management.base import BaseCommand
from myapp.models import Book

class Command(BaseCommand):
    help = 'Import books from JSON API'

    def handle(self, *args, **kwargs):
        with open('path/to/your/json_file.json', 'r') as f:
            data = json.load(f)
            for book_data in data['message']:
                Book.objects.create(
                    title=book_data['name'],
                    authors=book_data['author'],
                    isbn=book_data['isbn']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported books'))
