from rest_framework import serializers
from trains.models import Train
from cities.models import City
from routes.models import Route


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):
    from_city = CitiesSerializer(many=False)
    to_city = CitiesSerializer(many=False)

    class Meta:
        model = Train
        fields = (
            "id",
            "name",
            "from_city",
            "to_city",
            "travel_time",
        )


class RouteSerializer(serializers.ModelSerializer):
    from_city = CitiesSerializer(many=False)
    to_city = CitiesSerializer(many=False)
    trains = TrainSerializer(many=True)

    class Meta:
        model = Route
        fields = (
                "id",
                "name",
                "travel_times",
                "from_city",
                "to_city",
                "trains",
        )
