
def find_second_maximum(arr: list) -> int:
    first_max = arr[0]
    second_max = arr[0]

    if len(arr) < 2:
        return "Массив должен содержать хотя бы 2 элемента"

    for i in arr:
        if i > first_max:
            second_max = first_max
            first_max = i
        if i < second_max < first_max:
            second_max = i
    if second_max == first_max:
        return "Первый и второй максимум совпадают"
    return second_max

print(find_second_maximum([1, 2, 3, 4, 10, 11]))
print(find_second_maximum([2, 2, 2]))
print(find_second_maximum([1]))
