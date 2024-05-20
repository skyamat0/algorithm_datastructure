# バブルソートに似ている，左と右を比べるシェイカーソートとも．
from typing import List
import random

def cocktail_sort(numbers: List[int]) -> List[int]:
    start = 0
    end = len(numbers) - 1

    swap = True
    reverse = 0
    while swap:
        swap = False
        if reverse % 2 == 1:
            # 逆順にしてバブルソート
            # 小さいものを一番左に持っていく
            for i in range(end, start, -1):
                if numbers[i] > numbers[i-1]:
                    continue
                else:
                    numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
                    swap = True
            # 左に小さいものがくることが保証されているので，左端を一つ右にずらす
            start += 1
        else:
            # 通常のバブルソート
            # 大きいものを一番右に持っていく
            for i in range(start, end):
                if numbers[i] <= numbers[i+1]:
                    continue
                else:
                    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                    swap = True
            # 右に大きいものがくることが保証されているので，右端を一つ左にずらす
            end -= 1
        reverse += 1
    return numbers
        
        



if __name__ == "__main__":
    nums = [random.randint(0, 100) for _ in range(10)]
    print(nums)
    print(cocktail_sort(nums))