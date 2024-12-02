class BinarySearch:
    def __init__(self, arr, item):
        self.arr = arr
        self.item = item


    def binary_search(self):
        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = (low+high) // 2

            if self.item == self.arr[mid]:
                print(mid)
                return mid

            if self.arr[mid] > self.item:
                high = mid - 1

            else:
                low = mid + 1

        print(None)
        return None

