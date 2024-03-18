from trains.models import Train


def sort_routes(routes):
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    return sorted_routes[:5]
    # return sorted_routes


def find_route_total_time(right_ways, all_trains, travelling_time):
    routes = []
    for route in right_ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_trains[(route[i], route[i+1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= travelling_time:
            routes.append(tmp)
    if not routes:
        raise ValueError('Час у дорозі більше заданого. Збільшити час')
    return routes


def find_all_trains(qs):
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[q.from_city_id, q.to_city_id].append(q)
    return all_trains


def search_ways(all_ways, cities):
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Маршрут через ці міста неможливий')
        return right_ways
    else:
        right_ways = all_ways
        return right_ways


def dfs_paths(graph, start, goal):
    """шукає усі маршрути"""
    stack = [(start,[start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
              if next_ == goal:
                  yield path + [next_]
              else:
                  stack.append((next_, path + [next_]))


def get_graph(qs):

    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    # qs = Train.objects.all()
    qs = Train.objects.all().select_related('from_city', 'to_city')


    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']

    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_ways):
        raise ValueError('Маршруту, що задовольняє умовам не існує')

    right_ways = search_ways(all_ways, cities)

    all_trains = find_all_trains(qs)

    routes = find_route_total_time(right_ways, all_trains, travelling_time)

    sorted_routes = sort_routes(routes)
    context['routes'] = sorted_routes
    context['cities'] = {'from_city': from_city, 'to_city': to_city}

    return context