from sort import *


class SelectionSort(Sort):

    @measure
    def sort(self, to_sort):
        for current_index in range(len(to_sort)-1, 0, -1):
            position_of_max = self._find_max(to_sort, current_index)
            to_sort[current_index], to_sort[position_of_max] = to_sort[position_of_max], to_sort[current_index]
        return to_sort

    @staticmethod
    def _find_max(to_sort, current_index):
        position_of_max = 0
        for location in range(1, current_index + 1):
            if to_sort[location] > to_sort[position_of_max]:
                position_of_max = location

        return position_of_max

    def __str__(self):
        return 'selectionsort'
