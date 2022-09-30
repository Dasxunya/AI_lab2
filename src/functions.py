import colors as color

graph = {}
begin = 'Рига'
end = 'Одесса'


def set_default_value(d, key1):
    d.setdefault(key1, [])


def file_function(filename):
    """Ввод значений из файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            A_city = line.split(';')[0]
            B_city = line.split(';')[1]
            dist = line[:-1].split(';')[2]

            set_default_value(graph, A_city)
            set_default_value(graph, B_city)
            graph[A_city] = graph[A_city] + [(B_city, int(dist))]
            graph[B_city] = graph[B_city] + [(A_city, int(dist))]

    print('\nСвязи городов:')
    print(graph)
    limit = int(input('\nВведите значение лимита: '))

    """Вывод результатов работы методов"""
    print(color.BLUE + '\nПоиск в ширину' + color.PURPLE)
    bfs_search = bfs(graph, begin, end)
    print_list(bfs_search)

    print(color.BLUE + '\nПоиск в глубину' + color.PURPLE)
    dfs_search = dfs(graph, begin, end)
    print_list(dfs_search)

    print(color.BLUE + f'\nПоиск в глубину с лимитом = {limit}' + color.PURPLE)
    l_dfs = limited_dfs(graph, begin, end, limit)
    print_list(l_dfs)

    print(color.BLUE + '\nПоиск c итеративным углублением' + color.PURPLE)
    i_dfs = iterative_dfs(graph, begin, end)
    print_list(i_dfs)

    print(color.BLUE + f'\nДвунаправленный поиск' + color.PURPLE)
    bds(graph, begin, end)
    print(color.BLUE + f'Жадный поиск' + color.PURPLE)
    best_fs(graph, begin, end, odessa_data)
    print(color.BLUE + f'A* поиск' + color.PURPLE)
    astar_s(graph, begin, end, odessa_data)


def print_list(l):
    if (l is None) or (l is False):
        print('Такого пути нет')
    else:
        print(*l, sep=' -⮚ ', end=' 🚩\n')


def bfs(g, start, stop):
    visited = [start]
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == stop:
            return path
        childs = g[node]
        for child, d in childs:
            if child not in visited:
                visited.append(child)
                next_p = list(path)
                next_p.append(child)
                queue.append(next_p)
            if child != stop:
                continue
    return None


def dfs(g, start, stop, visited=None):
    if visited is None:
        visited = []
    if start == stop:
        return [start]
    for neighbor, d in g[start]:
        if neighbor not in visited:
            visited.append(start)
            path = dfs(g, neighbor, stop, visited)
            if path is not None:
                path.insert(0, start)
                return path
    return None


def limited_dfs(g, start, stop, limit, visited=None, order=0):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        if start == stop:
            return [start]

    if order >= limit:
        return None

    for child in set([a for a, _ in g[start]]) - set(visited):
        path = limited_dfs(g, child, stop, limit, visited, order + 1)
        if path:
            path.insert(0, start)
            return path

    return None


def iterative_dfs(g, start, stop):
    for cur_limit in range(1, len(g) + 1):

        path = limited_dfs(g, start, stop, limit=cur_limit, visited=[])
        if path:
            return path

    return None


def bds(g, start, stop):
    visited_f = [start]
    queue_f = [(start, 0)]

    visited_b = [stop]
    queue_b = [(stop, 0)]

    while queue_f and queue_b:
        current_f = queue_f.pop(0)
        current_b = queue_b.pop(0)

        print("{} {} Head ➥ {}".format(
            "".join(['\t' for i in range(current_f[1])]), current_f[1] + 1, current_f[0]), end=" -⮚ ")

        for (i, (child, _)) in enumerate(g[current_f[0]]):
            print(child, end=" ")
            if child not in visited_f:
                visited_f.append(child)
                queue_f.append((child, current_f[1] + 1))

        print()
        print("{} {} Tail ➥ {}".format(
            "".join(['\t' for i in range(current_b[1])]), current_b[1] + 1, current_b[0]), end=" -⮚ ")

        for (i, (child, _)) in enumerate(g[current_b[0]]):
            print(child, end=" ")
            if child not in visited_b:
                visited_b.append(child)
                queue_b.append((child, current_b[1] + 1))
        print()

        intersection = list(set(visited_f) & set(visited_b))
        if intersection:
            print(color.GREEN + "\n\t{} 🚩\n".format(", ".join(intersection)))
            return (visited_f, visited_b)
        else:
            print()

    return None


odessa_data = {
    'Брест': 806,
    'Вильнюс': 990,
    'Витебск': 969,
    'Волгоград': 1060,
    'Воронеж': 1020,
    'Даугавпилс': 1086,
    'Донецк': 560,
    'Житомир': 537,
    'Казань': 1641,
    'Калининград': 1506,
    'Каунас': 1340,
    'Киев': 443,
    'Кишинев': 157,
    'Минск': 855,
    'Москва': 1138,
    'Мурманск': 2504,
    'Ниж.Новгород': 1425,
    'Одесса': 0,
    'Орел': 817,
    'Рига': 1250,
    'С.Петербург': 1496,
    'Самара': 1581,
    'Симферополь': 313,
    'Таллинн': 1493,
    'Уфа': 1993,
    'Харьков': 564,
    'Ярославль': 1384
}


def best_fs(g, start, stop, f_n: dict):
    visited = [start]
    current = start
    counter = 0

    while current:
        counter += 1

        if current == stop:
            print("🚩", end="\n")
            return visited

        print("{}\t➥ {}".format(counter, current), end=" -⮚ ")

        heuristic_vals = []

        for (i, (child, _)) in enumerate(g[current]):
            heuristic_val = f_n[child]
            heuristic_vals.append((child, heuristic_val))
            if child == stop:
                print("{}:{}".format(child, heuristic_val), end=" 🚩\n\n")
                return
            else:
                print("{}:{}".format(child, heuristic_val), end=" ")

        heuristic_vals.sort(key=lambda x: x[1])

        for (next_candidate, _) in heuristic_vals:
            if next_candidate not in visited:
                visited.append(next_candidate)
                current = next_candidate
                break

        print()
    return None


def astar_s(g, start, stop, f_n: dict):
    #       узел | g(n) | h(n) | f(n) | order, где g(n) -по прямой, h(n) -эвристика, f(n) -общая
    queue = [(start, 0, 0, 0, 0)]
    visited = []
    counter = 0

    while queue:
        counter += 1

        queue.sort(key=lambda x: x[3])
        current = queue.pop(0)

        if current[0] not in visited:
            visited.append(current[0])

        if current[0] == stop:
            return visited

        print("{}{} ➥ {}".format("".join(['\t' for i in range(current[4])]), counter, current[0]), end=" -⮚ ")

        children = g[current[0]]

        for (child, distance) in children:

            sum_distance = current[1] + int(distance)
            heuristics = f_n[child]
            child_node = (child, sum_distance, heuristics, sum_distance + heuristics, current[4] + 1)

            if child in visited:
                continue

            print("{}:{}".format(child, child_node[3]), end=" ")
            if child == stop:
                print("🚩 ", end="\n")
                return

            if False in [not (node == child and child_node[3] > f) for (node, _, _, f, _) in queue]:
                continue
            else:
                queue.append(child_node)

        print()

    return None
