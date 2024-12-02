class Second_maximum:
    def __init__(self, arr):
        self.arr: list = arr

    def find_second_maximum(self) -> int:
        first_max = self.arr[0]
        second_max = self.arr[0]

        if len(self.arr) < 2:
            print(None)
            return None

        for i in self.arr:
            if i > first_max:
                second_max = first_max
                first_max = i
            if i < second_max < first_max:
                second_max = i
        if second_max == first_max:
            print(None)
            return None
        print(second_max)
        return second_max


