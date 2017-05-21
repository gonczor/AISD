from utils import timer


# @timer
def find_path(graph, vertex=0, start=True):
    if not graph:
        return []

    route = []
    if start:
        route.append(0)

    neighbours = graph[vertex]
    for neighbour in neighbours:
        # Remove from graph edge from vertex to its neighbour and save it to path
        route.append(graph[vertex].pop(graph[vertex].index(neighbour)))
        graph[neighbour].remove(vertex)
        # repeat for last added
        returned_route = find_path(graph, vertex=route[-1], start=False)
        route += returned_route
    return route
