def merge_sort (mas, ascending=True):
    if len(mas) < 2: # True - по возрастанию, False - по убыванию
        return mas
    else:
        left = merge_sort(mas[:int(len(mas)/2)], ascending)
        right = merge_sort(mas[int(len(mas)/2):], ascending)
        return merge(left, right, ascending)

def compare (a, b, ascending):
    if (a > b and ascending) or (a < b and not ascending):
        return 0
    else:
        return 1

def merge (left, right, ascending):
    i, j, result = 0, 0, []
    while i < len(left) and j < len(right):
        if compare(left[i], right[j], ascending):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
array = merge_sort(array, False)
print(array)
