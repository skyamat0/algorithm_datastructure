class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.length = 0
        
    def __len__(self):
        return self.length
        
    def __getitem__(self, i):
        return self.get(i)
        
    def __str__(self):
        _ = self.head.next_node
        i = 0
        while i < self.length:
            print(_.value)
            _ = _.next_node
            i += 1
        return "number of elements: " + str(self.length)
        
    def get(self, i):
        """
        ポインタを辿ってi番目の要素を取得
        """
        if i > self.length:
            raise IndexError
        j = 0
        target = self.head.next_node
        while j < i:
            target = target.next_node
            j += 1
        return target
        
    def insert(self, value, node=-1):
        """
        valueを持つノードをnode番目に挿入（デフォルトは末尾）
        """
        new_node = Node(value)
        if self.length == 0:
            self.head.next_node = new_node
            new_node.next_node = None
            self.tail.next_node = new_node
            self.length += 1
            return self

        if node == 0:
            self.insert_head(new_node)

        elif node == -1:
            self.insert_tail(new_node)

        else:
            node = self.get(node)
            new_node.next_node = node.next_node
            node.next_node = new_node
        self.length += 1
        return self
        
    def insert_head(self, new_node):
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node
    
    def insert_tail(self, new_node):
        self.tail.next_node.next_node = new_node
        self.tail.next_node = new_node
    
    def delete(self, node=-1):
        """
        ポインタを変えることで、ノードを削除（デフォルトは末尾）
        """
        if node == -1 or node == self.length-1:
            self.tail.next_node = self.get(self.length-1)
        elif node == 0:
            self.head.next_node = self.head.next_node.next_node
        else:
            self.get(node-1).next_node  = self.get(node+1)
        self.length -= 1
        return self


    
if __name__ == "__main__":
    l = LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4, 0)
    l.insert(1)
    l.insert(5)
    l.delete(3)
    l.delete(0)
    l.delete(-1)
    l.delete(2)
    print(l)
