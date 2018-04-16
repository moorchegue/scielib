from rest_framework import filters, viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from ..models.book_author import BookAuthor
from ..serializers.book_author import BookAuthorSerializer


class BookAuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows book authors to be viewed or edited.
    """

    queryset = BookAuthor.objects.all()

    serializer_class = BookAuthorSerializer

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    filter_fields = (
        'id',
    )
    search_fields = (
        'name',
    )
