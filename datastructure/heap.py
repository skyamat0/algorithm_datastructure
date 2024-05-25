import heapq
class Heap:
    def __init__(self, l=[], order="min"):
        self.heap = l
    
    def insert(self, data):
        if len(self.heap) == 0:
            self.heap.append(data)
        else:

        
    def swap(self, l, i, j):
        """
        配列のi番目の要素とj番目の要素をswapする
        """
        l[j], l[i] = l[i], l[j]
        return l

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 0]
    """
                    1
        2                       3
    4       5               6       2
    """
    print(Heap().swap(l, 1, 5))
    print(l)

    #ind: 5, 6 -> ind 2
    #ind: 7, 8 -> ind 3
    #ind: 9, 10 -> ind 4 
