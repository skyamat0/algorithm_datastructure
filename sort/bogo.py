#概要：テキトーに並べ替える
import random
from typing import List

def in_order(numbers: List[int]) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            # 今見ているものよりも右のインデックスの数値が大きければFalse
            return False
    return True

def in_order_oneliner(numbers: List[int]) -> bool:
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order_oneliner(numbers):
        random.shuffle(numbers)
    return numbers

if __name__=="__main__":
    random.seed(10)
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(bogo_sort(nums))