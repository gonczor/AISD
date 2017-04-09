import random
import unittest

from sort.heapsort import HeapSort
from sort.insertion import InsertionSort
from sort.iterativeQuicksort import IterativeQuickSort
from sort.mergesort import MergeSort
from sort.recursiveQuicksort import RecursiveQuickSort
from sort.selection import SelectionSort


class SortTestCase(unittest.TestCase):
    """
    On initialization a random list is created. It is then copied in setUp to to_sort list before each algorithm runs
    This allows to check each algorithm on huge amount of same data.
    """

    def __init__(self, *args):
        super().__init__(*args)

        self.TO_SORT_LEN = 5000

        self.random_list = []
        for i in range(self.TO_SORT_LEN):
            self.random_list.append(random.randint(0, 1000))

    def setUp(self):
        self.to_sort = self.random_list[:]

    def test_insertion_sort(self):
        insertion_sort = InsertionSort()
        self.to_sort = insertion_sort.sort(self.to_sort)
        self._assert_to_sort_gets_sorted_ascending()

    def test_selection_sort(self):
        selection_sort = SelectionSort()
        self.to_sort = selection_sort.sort(self.to_sort)
        self._assert_to_sort_gets_sorted_ascending()

    def test_heap_sort(self):
        heap_sort = HeapSort()
        self.to_sort = heap_sort.sort(self.to_sort)
        self._assert_to_sort_gets_sorted_ascending()

    def test_merge_sort(self):
        merge_sort = MergeSort()
        self.to_sort = merge_sort.sort(self.to_sort)
        self._assert_to_sort_gets_sorted_ascending()

    def test_recursive_quick_sort(self):
        quick_sort = RecursiveQuickSort()
        self.to_sort = quick_sort.sort(self.to_sort)
        self._assert_to_sort_gets_sorted_ascending()

    def test_iterative_quick_sort(self):
        quick_sort = IterativeQuickSort()
        self.to_sort = quick_sort.sort(self.to_sort)
        self._assert_to_sort_gets_sorted_ascending()

    def _assert_to_sort_gets_sorted_ascending(self):
        for i in range(1, self.TO_SORT_LEN):
            self.assertGreaterEqual(self.to_sort[i], self.to_sort[i-1])
