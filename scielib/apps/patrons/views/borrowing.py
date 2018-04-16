from rest_framework import viewsets
from rest_framework import response
from rest_framework.decorators import detail_route
from url_filter.integrations.drf import DjangoFilterBackend

from ..models.borrowing import Borrowing
from ..serializers.borrowing import BorrowingSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows borrowings to be viewed or edited.
    """

    queryset = Borrowing.objects.all(
        ).select_related(
            'book',
            'patron',
        )

    serializer_class = BorrowingSerializer

    filter_backends = (
        DjangoFilterBackend,
    )
    filter_fields = (
        'id',
        'book',
        'patron',
        'borrowed_at',
        'got_back_at',
    )

    @detail_route(methods=['patch'])
    def get_back(self, request, pk=None):
        """
        Get a book back.
        """
        borrowing = self.get_object()
        borrowing.get_back()

        return response.Response({'ok': 'got back'})
