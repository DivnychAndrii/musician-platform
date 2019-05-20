from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.pagination import ResultSetPagination
from demand.models import Demand
from demand.serializers import DemandSerializer


class DemandViewSet(viewsets.ModelViewSet):

    serializer_class = DemandSerializer
    queryset = Demand.objects.get_queryset().order_by('id')
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = ResultSetPagination
    # renderer_classes = (JSONRenderer, )