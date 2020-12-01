from rest_framework import serializers

from books_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ('title', 'author')
        fields = '__all__'
