def generate_min(size):
    graph = [[] for _ in range(size)]
    for i in range(size):
        if i != 0:
            if i-1 not in graph[i] and i not in graph[i-1]:
                graph[i].append(i-1)
                graph[i-1].append(i)
        else:
            if i not in graph[size-1] and size-1 not in graph[i]:
                graph[i].append(size-1)
                graph[size-1].append(i)
    return graph


def generate_max(size):
    connections = []
    if size % 2 == 0:
        for i in range(size-1):
            connections.append([j for j in range(size)])
            connections[i].remove(i)
        connections.append([0, size-2])
    else:
        raise Exception('Zjebało się')
        # for i in range(size):
        #     connections.append([j for j in range(size)])
        #     connections[i].remove(i)
    return connections
