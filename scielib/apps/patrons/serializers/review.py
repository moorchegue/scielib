from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.review import Review


class ReviewSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = Review
        fields = (
            'url',
            'id',
            'book',
            'patron',
            'review_text',
            'review_score',
        )
