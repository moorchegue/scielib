from rest_framework import filters, viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from ..models.book_category import BookCategory
from ..serializers.book_category import BookCategorySerializer


class BookCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows book categories to be viewed or edited.
    """

    queryset = BookCategory.objects.all()

    serializer_class = BookCategorySerializer

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
