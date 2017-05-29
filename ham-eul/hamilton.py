from utils import timer

path = []
found_path = False


@timer
def find_all_paths_start(graph):
    find_all_paths(graph)


def find_all_paths(graph, current_vertex=0):
    global path, found_path
    number_of_vertices = len(graph)
    neighbours = graph[current_vertex]

    path.append(current_vertex)
    for neighbour in neighbours:
        if neighbour not in path:
            find_all_paths(graph, neighbour)

    # If all have been found and there is edge from current vertex to the beginning
    if len(path) == number_of_vertices and 0 in graph[current_vertex]:
        # print(path) too much output
        pass
    path.pop()


@timer
def find_path_start(graph, current_vertex=0):
    find_path(graph)


def find_path(graph, current_vertex=0):
    global path, found_path
    number_of_vertices = len(graph)
    neighbours = graph[current_vertex]

    path.append(current_vertex)
    for neighbour in neighbours:
        if neighbour not in path:
            find_path(graph, neighbour)
            if found_path:
                return

    # If all have been found and there is edge from current vertex to the beginning
    if len(path) == number_of_vertices and 0 in graph[current_vertex]:
        found_path = True
        return
    else:
        path.pop()
