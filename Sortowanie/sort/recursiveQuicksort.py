from . import *


class RecursiveQuickSort(QuickSort):

    @measure
    def sort(self, to_sort):
        return self._quick_sort(to_sort, 0, len(to_sort)-1)

    def _quick_sort(self, to_sort, left, right):
        if left < right:
            pivot_position = self._partition(to_sort, left, right)
            self._quick_sort(to_sort, left, pivot_position-1)
            self._quick_sort(to_sort, pivot_position+1, right)
            return to_sort

    def __str__(self):
        return 'recursive quicksort'
