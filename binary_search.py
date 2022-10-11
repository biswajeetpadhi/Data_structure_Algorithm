
import math


def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    middle = math.floor((start+end)/2)


    #arr = sorted(arr)

    print(arr)
    while arr[middle] != num and start <= end:
        if num < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end)/2)

    if arr[middle] == num:
        return middle
    else:
        return -1





if __name__ == "__main__":
    #print(binary_search([2, 6, 8, 34, 78, 267, 743], 34))
    l = [3,56,7,8]
    print(l[0,-1])