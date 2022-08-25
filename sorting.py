
def bubble_sort(b_list):
    n = len(b_list)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if b_list[j] > b_list[j + 1]:
                b_list[j], b_list[j + 1] = b_list[j + 1], b_list[j]
                already_sorted = False
        if already_sorted:
            break
    return b_list


if __name__ == "__main__":
    print(bubble_sort([2, 7, 4]))

    """
    print(sorted([4, 6, 2, 6, 2]))
    a = [3, 5, 2, 7, 3, 6, 9]
    a.sort()
    print(a)
    """