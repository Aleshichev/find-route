from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from cities.forms import CityForm
from cities.models import City
from braces.views import CsrfExemptMixin
from django.contrib import messages
from django import forms
import re
from django.core.exceptions import ValidationError


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"


# class CityCreateView(
#     CsrfExemptMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView
# ):
#     model = City
#     form_class = CityForm
#     template_name = "cities/create.html"
#     success_url = reverse_lazy("cities:home")
#     success_message = "Місто вдало створено"
 
    
def city_create_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not name.replace(" ", "").isalpha():
                messages.error(request, "Назва міста має містити тільки букви")
            else:
                city = form.save()
                messages.success(request, "Місто вдало створено")
                return redirect('cities:home')
    else:
        form = CityForm()
    
    return render(request, 'cities/create.html', {'form': form})

class CityUpdateView(
    CsrfExemptMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView
):
    model = City
    form_class = CityForm
    template_name = "cities/update.html"
    success_url = reverse_lazy("cities:home")
    success_message = "Місто вдало відредаговано"


class CityDeleteView(
    CsrfExemptMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView
):
    model = City
    template_name = "cities/delete.html"
    success_url = reverse_lazy("cities:home")
    success_message = "Місто вдало видалено"


class CityListView(ListView):
    paginate_by = 5
    model = City
    template_name = "cities/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context["form"] = form
        return context
