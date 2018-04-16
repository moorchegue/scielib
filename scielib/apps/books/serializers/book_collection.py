from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.book_collection import BookCollection


class BookCollectionSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = BookCollection
        fields = (
            'url',
            'id',
            'name',
            'description',
        )
