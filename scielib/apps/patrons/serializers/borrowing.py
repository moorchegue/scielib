from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.borrowing import Borrowing


class BorrowingSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = Borrowing
        fields = (
            'url',
            'id',
            'book',
            'patron',
            'borrowed_at',
            'got_back_at',
        )
