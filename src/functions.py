import colors as color

cities_names = ['Вильнюс', 'Витебск', 'Воронеж', 'Волгоград', 'Калининград', 'Каунас', 'Киев', 'Житомир', 'Кишинев',
                'С.Петербург', 'Москва', 'Мурманск', 'Орел', 'Одесса', 'Рига', 'Таллинн', 'Харьков', 'Ярославль',
                'Уфа', 'Брест', 'Ниж.Новгород', 'Даугавпилс', 'Донецк', 'Казань', 'Минск', 'Симферополь', 'Самара']
cities = {cities_names[i]: i for i in range(len(cities_names))}
graph = {}
start = 'Рига'
end = 'Одесса'


def set_value(d, keys, value):
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = value


def file_function(filename):
    """Ввод значений из файла"""
    visited = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            A_city = line.split(';')[0]
            B_city = line.split(';')[1]
            dist = line[:-1].split(';')[2]  #:-1 срез для удаления \n

            keys = [A_city, B_city]
            set_value(graph, keys, int(dist))
            keys = [B_city, A_city]
            set_value(graph, keys, int(dist))

    """Вывод результатов работы методов"""
    dfs_search = dfs(graph, start, end, visited)
    print(color.PURPLE)
    print(*dfs_search, sep='-->')


def dfs(g, current, goal, visited):
    if current == goal:
        return [current]
    if current in g:
        for neighbor in g[current].keys():
            if neighbor not in visited:
                visited[current] = 1
                path = dfs(g, neighbor, goal, visited)

                if path is not None:
                    path.insert(0, current)
                    return path
    return None
