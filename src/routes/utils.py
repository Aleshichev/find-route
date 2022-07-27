from trains.models import Train
# {21: {22}, 22: {24, 26}, 25: {23}, 18: {24, 25}, 2: {18, 22}, 26: {2}, 28: {2}}


def dfs_paths(graph, start, goal):
    """ищет набор всех возможных маршрутов/ возвращает генератор"""
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
    """функция создаёт граф"""
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())    # значение из какого города идёт поезд если такой ключ не существует
        graph[q.from_city_id].add(q.to_city_id)    # добавляем куда приедет поезд
    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Train.objects.all().select_related('from_city', 'to_city')   # список всех поездов из бд
    graph = get_graph(qs)
    data = form.cleaned_data      # берём значения из функции
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']
    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))    #все возможные пути
    if not len(all_ways):
        raise ValueError('Маршрута, удовлетворяющего условиям не существует')
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)      # добавляет город в список если это возможно
            if not right_ways:
                raise ValueError('Маршрут через эти города не возможен')
    else:
        right_ways = all_ways
    routes = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[q.from_city_id, q.to_city_id].append(q)
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
        raise ValueError('Время в пути больше заданного. Увеличьте время')
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
    context['routes'] = sorted_routes
    context['cities'] = {'from_city': from_city, 'to_city': to_city}
    return context