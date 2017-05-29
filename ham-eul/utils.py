import time

duration = []


def timer(func):
    def _timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration.append(end-start)
        return result
    return _timer


def get_average(times):
    return sum(times)/len(times)


def to_neighbourhood():
    data =   """0 0 3 6 5 7
                0 0 4 3 0 0
                3 4 0 0 3 2
                6 3 0 0 2 5
                5 0 3 2 0 1
                7 0 2 5 1 0"""

    neighbourhoods = [[] for _ in range(6)]
    matrix = [[]]
    for line in data.splitlines():
        for value in line.split():
            if value != '0':
                matrix[-1].append(True)
            else:
                matrix[-1].append(False)
        matrix.append([])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                neighbourhoods[i].append(j)

    return neighbourhoods
