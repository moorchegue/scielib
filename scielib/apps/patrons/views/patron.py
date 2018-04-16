from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from ..models.patron import Patron
from ..serializers.patron import PatronSerializer


class PatronViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patrons to be viewed or edited.
    """

    queryset = Patron.objects.all()

    serializer_class = PatronSerializer

    filter_backends = (
        DjangoFilterBackend,
    )
    filter_fields = (
        'id',
    )
