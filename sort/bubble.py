# 左と右を比べ続ける
# O(n^2)
from typing import List
import random

def bubble_sort(numbers: List[int]) -> List[int]:
    l = len(numbers)
    for i in range(l):
        for j in range(l-i-1):
            if numbers[j] <= numbers[j+1]:
                continue
            else:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == "__main__":
    nums = [random.randint(0, 10) for _ in range(5)]
    print(nums)
    print(bubble_sort(nums))
