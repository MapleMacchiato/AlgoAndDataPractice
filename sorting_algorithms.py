def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    arr = r_merge_sort(arr)
    return arr


def r_merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = r_merge_sort(arr[:mid])
    right = r_merge_sort(arr[mid:])
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        elif left[i] == right[j]:
            res.append(left[i])
            res.append(right[j])
            i += 1
            j += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def quick_sort(arr):
    arr.sort()
    return arr


a = [9, 6, 5, -1, 7, 2, 1, 4, 3, 8]
b = quick_sort(a)
print(b)
