from utils.measure import measure


class Sort:

    def sort(self, to_sort):
        raise NotImplementedError


class QuickSort(Sort):
    """
    Pivot chosen as most right element
    """

    def sort(self, to_sort):
        raise NotImplementedError

    @staticmethod
    def _partition(to_sort, left, right):
        pivot_value = to_sort[right]
        left_local = left
        right_local = right

        while True:
            while right_local >= left_local and to_sort[right_local] >= pivot_value:
                right_local -= 1
            while left_local <= right_local and to_sort[left_local] <= pivot_value:
                left_local += 1

            # smaller elements on the left and bigger are on the right
            if right_local <= left_local:
                break

            to_sort[left_local], to_sort[right_local] = to_sort[right_local], to_sort[left_local]

        # change with pivot
        to_sort[right], to_sort[left_local] = to_sort[left_local], to_sort[right]
        return left_local
