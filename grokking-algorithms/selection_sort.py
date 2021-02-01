from random import randint


def selection_sort(arr):
    for idx in range(len(arr)):
        cut = arr[idx:]
        m = min(cut)
        i = cut.index(m) + idx
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr


if __name__ == "__main__":
    for _ in range(20):
        length = randint(1, 20)
        test_array = x = [randint(-100, 99) for p in range(length)]
        assert(selection_sort(test_array) == sorted(test_array))
