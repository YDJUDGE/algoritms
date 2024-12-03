class BinarySearch:
    def __init__(self, arr, item):
        if arr != sorted(arr):
            ValueError("Arr not sorted for binary search")
        self.arr = arr
        self.item = item


    def binary_search(self):
        """
        Бинарный поиск, на вход принимается массив и значение, искомое.
        arr - массив
        item - искомое значение
        :return:
        """
        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = (low+high) // 2

            if self.item == self.arr[mid]:
                return mid

            if self.arr[mid] > self.item:
                high = mid - 1

            else:
                low = mid + 1

        return None
