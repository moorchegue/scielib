from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.book import Book


class BookSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = Book
        fields = (
            'url',
            'id',
            'category',
            'genres',
            'collections',
            'authors',
            'cover',
            'name',
            'isbn',
            'edition',
            'published_at',
            'stock',
            'borrowing_price',
        )
