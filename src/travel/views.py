from rest_framework import viewsets, mixins
from cities.models import City
from trains.models import Train
from routes.models import Route
from travel.serializers import TrainSerializer, CitiesSerializer, RouteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly
from rest_framework.viewsets import GenericViewSet



class TrainViewSet(viewsets.ModelViewSet):
    # queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Train.objects.all()
        
        return Train.objects.filter(pk=pk)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return City.objects.all()
        
        return City.objects.filter(pk=pk)


class RouteViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Route.objects.all()
        
        return Route.objects.filter(pk=pk)
