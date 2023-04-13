from rest_framework import generics, viewsets
from cities.models import City
from trains.models import Train
from routes.models import Route
from travel.serializers import TrainSerializer, CitiesSerializer, RouteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly


class TrainViewSet(viewsets.ModelViewSet):
    # queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Train.objects.all()[:5]
        
        return Train.objects.filter(pk=pk)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return City.objects.all()[:5]
        
        return City.objects.filter(pk=pk)


class RouteViewSet(viewsets.ModelViewSet):
    # queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Route.objects.all()[:5]
        
        return Route.objects.filter(pk=pk)
