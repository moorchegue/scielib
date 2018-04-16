from rest_framework import filters, viewsets
from rest_framework import response
from rest_framework.decorators import detail_route
from url_filter.integrations.drf import DjangoFilterBackend

from ..models.book import Book
from ..serializers.book import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """

    queryset = Book.objects.all(
        ).select_related(
            'category',
        ).prefetch_related(
            'genres',
            'collections',
            'authors',
        )

    serializer_class = BookSerializer

    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    filter_fields = (
        'id',
        'book_category',
    )
    search_fields = (
        'name',
    )

    @detail_route(methods=['patch'])
    def borrow(self, request, pk=None):
        """
        Borrow a book as a current user.
        """
        book = self.get_object()
        book.borrow_to(request.user.patron)

        return response.Response({'ok': 'borrowed'})

    @detail_route(methods=['patch'])
    def get_back(self, request, pk=None):
        """
        Get back a book as a current user.
        """
        book = self.get_object()
        book.get_back(request.user.patron)

        return response.Response({'ok': 'borrowed'})
