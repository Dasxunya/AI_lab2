import colors as color

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
    bfs_search = bfs(graph, start, end)
    print('\nПоиск в глубину: ' + color.PURPLE)
    print_list(dfs_search)
    print(color.BLUE + 'Поиск в ширину: ' + color.PURPLE)
    print_list(bfs_search)


def print_list(l):
    if l is None:
        print('Такого пути нет')
    else:
        print(*l, sep=' --> ')


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


def bfs(g, current, goal):
    q = [[current]]
    while q:
        path = q.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for n in g.get(node, []):
            next_p = list(path)
            next_p.append(n)
            q.append(next_p)
