from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Host
from .serializers import HostListSerializer, HostDetailSerializer


class ShowHost(ReadOnlyModelViewSet):
    queryset = Host.objects.all()
    # serializer_class = HostListSerializer

    # lookup_field = 'pk'

    serialzers = {
        'list': HostListSerializer,
        'retrieve': HostDetailSerializer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)

