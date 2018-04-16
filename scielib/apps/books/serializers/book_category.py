from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.book_category import BookCategory


class BookCategorySerializer(HyperlinkedModelSerializer):

    class Meta:

        model = BookCategory
        fields = (
            'url',
            'id',
            'name',
            'description',
        )
