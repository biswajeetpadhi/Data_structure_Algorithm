
from typing import  List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance = 0

        for num1 in arr1:

            is_qualify = True
            for num2 in arr2:
                diff = abs(num1 - num2)

                if diff <= d:
                    is_qualify = False
                    break

            if is_qualify:
                distance += 1

        return distance


obj = Solution()

arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2

if __name__ == "__main__":
    print(obj.findTheDistanceValue(arr1, arr2, d))
