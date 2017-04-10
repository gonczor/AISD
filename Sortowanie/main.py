#!/usr/bin/env python3
import os
import sys

from Sortowanie.sort.heapsort import HeapSort
from Sortowanie.sort.insertion import InsertionSort
from Sortowanie.sort.iterativeQuicksort import IterativeQuickSort
from Sortowanie.sort.mergesort import MergeSort
from Sortowanie.sort.recursiveQuicksort import RecursiveQuickSort
from Sortowanie.sort.selection import SelectionSort
from Sortowanie.utils.measure import time_elapsed
from Sortowanie.utils.generator import generate_data
from Sortowanie.common import *


def run():
    algorithms = get_algorithms()
    for algorithm in algorithms:
        test_algorithm(algorithm)


def get_algorithms():
    insertion_sort = InsertionSort()
    selection_sort = SelectionSort()
    heap_sort = HeapSort()
    merge_sort = MergeSort()
    recursive_quick = RecursiveQuickSort()
    iterative_quick = IterativeQuickSort()
    return insertion_sort, selection_sort, heap_sort, merge_sort, recursive_quick, iterative_quick


def test_algorithm(algorithm):
    for data_type in data_types:
        measure_path = os.path.join(measurement_directory, str(algorithm))
        measure(algorithm=algorithm, measure_path=measure_path, data_type=data_type)


def measure(algorithm, measure_path, data_type):
    for size in list_sizes:
        # to save times
        test_output = []
        for i in range(test_points_number):
            path_to_data = os.path.join(data_directory_name, data_type, str(size), str(i))
            data_file = open(path_to_data)
            tmp = []
            # build array to sort
            for line in data_file:
                tmp.append(int(line))
            algorithm.sort(tmp)
            test_output.append(time_elapsed.pop())
            data_file.close()

        total_time = 0.0
        for local_time in test_output:
            total_time += local_time
        if not os.path.exists(measure_path):
            os.makedirs(measure_path)

        output_file_path = os.path.join(measure_path, data_type)
        if not os.path.exists(output_file_path):
            output_file = open(output_file_path, 'w')
        else:
            output_file = open(output_file_path, 'a')
        output_file.write('{}\t{}\n'.format(size, str(total_time / test_points_number)))
        output_file.close()


if __name__ == '__main__':
    if '--generate' in sys.argv or '-g' in sys.argv:
        generate_data()
    else:
        run()
