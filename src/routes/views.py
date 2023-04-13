from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from cities.models import City
from routes.forms import RouteForm, RouteModelForm
from routes.models import Route
from routes.utils import get_routes
from trains.models import Train
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


@csrf_exempt
def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Немаэ данних для пошуку')
        return render(request, 'routes/home.html', {'form': form})

@csrf_exempt
@login_required
def add_route(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from-city'])
            to_city_id = int(data['to-city'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_lst).select_related(
                'from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(initial={'from_city': cities[from_city_id],
                                           'to_city': cities[to_city_id],
                                           'travel_times': total_time,
                                           'trains': qs
                                           })
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'Неможливо зберегти неіснуючий маршрут')
        return redirect('/')

@csrf_exempt
def save_route(request):
    if request.method == "POST":
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Маршрут вдало збережено')
            return redirect('/')
        else:
            messages.error(request, 'Маршрут з цією назвою вже існує')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'Неможливо зберегти неіснуючий маршрут')
        return redirect('/')


class RouteListView(ListView):
    paginate_by = 3
    model = Route
    template_name = 'routes/list.html'


class RouteDetailView(CsrfExemptMixin, DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'


class RouteDeleteView(CsrfExemptMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Route
    template_name = 'routes/delete.html'
    success_url = reverse_lazy('home')
    success_message = "Маршрут вдало видалено"
