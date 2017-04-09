from . import *


class InsertionSort(Sort):

    @measure
    def sort(self, to_sort: list):
        for i in range(1, len(to_sort)):
            if to_sort[i] < to_sort[i-1]:
                self._move_until_lower_is_found(to_sort, i)
        return to_sort

    @staticmethod
    def _move_until_lower_is_found(to_sort, position):
        while position > 0 and to_sort[position] < to_sort[position - 1]:
            to_sort[position], to_sort[position - 1] = to_sort[position - 1], to_sort[position]
            position -= 1

    def __str__(self):
        return 'insertionsort'
