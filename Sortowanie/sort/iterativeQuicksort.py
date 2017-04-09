from . import *


class IterativeQuickSort(QuickSort):

    @measure
    def sort(self, to_sort):
        return self._quick_sort(to_sort, 0, len(to_sort)-1)

    def _quick_sort(self, to_sort, left, right):
        stack = [(left, right)]

        while stack:
            (left, right) = stack.pop()
            pivot = self._partition(to_sort, left, right)

            if pivot - 1 > left:
                stack.append((left, pivot - 1))

            if pivot + 1 < right:
                stack.append((pivot + 1, right))

        return to_sort

    def __str__(self):
        return 'iterative quicksort'
