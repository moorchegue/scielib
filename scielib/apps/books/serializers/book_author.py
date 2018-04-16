from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.book_author import BookAuthor


class BookAuthorSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = BookAuthor
        fields = (
            'url',
            'id',
            'name',
            'bio',
        )
