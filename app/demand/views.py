from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from app.pagination import ResultSetPagination
from demand.models import Demand
from demand.serializers import DemandSerializer


class DemandViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = DemandSerializer
    queryset = Demand.objects.get_queryset().order_by('id')
    permission_classes = [IsAuthenticated]
    pagination_class = ResultSetPagination
    # renderer_classes = (JSONRenderer, )
