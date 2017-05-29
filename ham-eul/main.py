import os
import sys

import utils
from generator import *
import euler
import hamilton

for i in range(5, 21):
    graph = generate_min(i*10)

    for _ in range(5):
        euler.find_path_start(graph[:])
    with open(os.path.join('output', 'euler', 'min'), 'a') as f:
        f.write('{}\t{}\n'.format(i*10, utils.get_average(utils.duration)))
    utils.duration = []

    for _ in range(5):
        hamilton.find_path_start(graph[:])
    with open(os.path.join('output', 'hamilton', 'min'), 'a') as f:
        f.write('{}\t{}\n'.format(i*10, utils.get_average(utils.duration)))
    utils.duration = []

for i in range(5, 21):
    graph = generate_max(i*10)

    for _ in range(5):
        euler.find_path_start(graph[:])
    with open(os.path.join('output', 'euler', 'max'), 'a') as f:
        f.write('{}\t{}\n'.format(i*10, utils.get_average(utils.duration)))
    utils.duration = []

    for _ in range(5):
        hamilton.find_path_start(graph[:])
    with open(os.path.join('output', 'hamilton', 'max'), 'a') as f:
        f.write('{}\t{}\n'.format(i*10, utils.get_average(utils.duration)))
    utils.duration = []

# for i in range(5, 21):
#     graph = generate_half(i*10)
# 
#     for _ in range(5):
#         hamilton.find_all_paths_start(graph[:])
#     with open(os.path.join('output', 'hamilton_all', 'all'), 'a') as f:
#         f.write('{}\t{}\n'.format(i*10, utils.get_average(utils.duration)))
#     utils.duration = []
