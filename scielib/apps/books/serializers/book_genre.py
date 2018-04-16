from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.book_genre import BookGenre


class BookGenreSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = BookGenre
        fields = (
            'url',
            'id',
            'name',
            'description',
        )
