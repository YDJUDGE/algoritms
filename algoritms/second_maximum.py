class Second_maximum:
    def __init__(self, arr):
        self.arr: list = arr

    def find_second_maximum(self) -> int:
        """
        Принимается на вход первое число массива и сторое, после они последовательно сравниваются.
        Таким образом вычисляется второй максимум.
        first_max - первый
        second_max - второй
        :return:
        """
        if len(self.arr) < 2:
            return None

        first_max = self.arr[0]
        second_max = self.arr[0]

        for i in self.arr:
            if i > first_max:
                second_max = first_max
                first_max = i
            if i < second_max < first_max:
                second_max = i
        if second_max == first_max:
            return None
        return second_max


