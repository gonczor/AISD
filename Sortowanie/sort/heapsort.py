from . import *


class HeapSort(Sort):
    to_sort = []

    @measure
    def sort(self, to_sort):
        self.to_sort = to_sort
        self._convert_to_heap()
        self._get_sorted_list()
        return self.to_sort

    def _convert_to_heap(self):
        length = len(self.to_sort) - 1
        last_parent = length // 2
        for i in range(last_parent, -1, -1):
            self._make_heap(i, length)

    def _get_sorted_list(self):
        length = len(self.to_sort) - 1
        for i in range(length, 0, -1):
            if self.to_sort[0] > self.to_sort[i]:
                self.to_sort[0], self.to_sort[i] = self.to_sort[i], self.to_sort[0]
                self._make_heap(0, i - 1)

    def _make_heap(self, first, last):
        largest = 2 * first + 1
        while largest <= last:
            if self._right_child_exists_and_is_larger_than_left(largest, last):
                largest += 1

            if self._child_larger_than_parent(largest, first):
                self.to_sort[largest], self.to_sort[first] = self.to_sort[first], self.to_sort[largest]
                first = largest
                largest = 2 * first + 1
            else:
                return

    def _right_child_exists_and_is_larger_than_left(self, largest, last):
        return (largest < last) and (self.to_sort[largest] < self.to_sort[largest + 1])

    def _child_larger_than_parent(self, largest, first):
        return self.to_sort[largest] > self.to_sort[first]

    def __str__(self):
        return 'heapsort'
