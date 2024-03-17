from django.urls import path

from cities.views import CityListView, city_create_view, \
    CityDetailView, CityUpdateView, CityDeleteView

urlpatterns = [
    path('', CityListView.as_view(), name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('add/', city_create_view, name='create'),  
]