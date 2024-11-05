class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglelyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current.next is None:
                    self.tail = prev
                return True
            prev = current
            current = current.next
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def traversal(self):
        print('\nLinked list:')
        for data in self:
            print( data, end=' -> ')
        print('End')

    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head 
            self.head = new_node        # new node just created becomes head of linked list 
            if not self.tail:
                self.tail = new_node
        else:
            current = self.head
            previous = None
            current_position = 0
            while current is not None and current_position < position:
                previous = current
                current = current.next
                current_position += 1
            previous.next = new_node
            new_node.next = current
            if current is None:
                self.tail = new_node


linkedList = SinglelyLinkedList()
linkedList.append([1, 2, 3])
linkedList.append({'a': 4, 'z': [1, 2, 3], 'f': {'a':2, 'b': 10}})
linkedList.append(1)
# linkedList.delete(1) 
linkedList.insert(1, [1])
linkedList.traversal()
print('\nSinglely Linked List Node 1 (Head):', linkedList.head.data)
print('Singlely Linked List Node 2:', linkedList.head.next.data)
print('Singlely Linked List Node 3 (Tail):', linkedList.head.next.next.data)


