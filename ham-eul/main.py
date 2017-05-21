from generator import *
import euler

# graph = generate_min(5)
# print('Graph: {}'.format(graph))
# print(euler.find_path(graph))
# print('###')
graph = generate_max(6)
print('Graph: {}'.format(graph))
print(euler.find_path(graph))
