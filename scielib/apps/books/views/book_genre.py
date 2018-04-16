from rest_framework import filters, viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from ..models.book_genre import BookGenre
from ..serializers.book_genre import BookGenreSerializer


class BookGenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows book genres to be viewed or edited.
    """

    queryset = BookGenre.objects.all()

    serializer_class = BookGenreSerializer

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
