from rest_framework.serializers import HyperlinkedModelSerializer

from ..models.patron import Patron


class PatronSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = Patron
        fields = (
            'url',
            'id',
        )
