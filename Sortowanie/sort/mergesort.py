from . import *


class MergeSort(Sort):

    @measure
    def sort(self, to_sort):
        return self._merge_sort(to_sort)

    def _merge_sort(self, to_sort):
        if len(to_sort) > 1:
            middle_index = len(to_sort) // 2
            right_half = to_sort[:middle_index]
            left_half = to_sort[middle_index:]

            right_half = self._merge_sort(right_half)
            left_half = self._merge_sort(left_half)

            return self._merge(left_half, right_half)
        else:
            return to_sort

    @staticmethod
    def _merge(left_half, right_half):
        merged_list = []
        left_index = right_index = 0

        left_length = len(left_half)
        right_length = len(right_half)

        while left_index < left_length and right_index < right_length:
            if left_half[left_index] < right_half[right_index]:
                merged_list.append(left_half[left_index])
                left_index += 1

            else:
                merged_list.append(right_half[right_index])
                right_index += 1

        while left_index < left_length:
            merged_list.append(left_half[left_index])
            left_index += 1

        while right_index < right_length:
            merged_list.append(right_half[right_index])
            right_index += 1

        return merged_list

    def __str__(self):
        return 'mergesort'
