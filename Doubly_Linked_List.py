class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def insert(self, position, data):
        print(f'\nNode data: {data} inserted at position: {position}')
        new_node = Node(data)
        if position == 0: #head
            new_node.next = self.head 
            new_node.next.prev = new_node
            self.head = new_node        # new node just created becomes head of linked list 
            if not self.tail:
                self.tail = new_node
        else:
            current = self.head
            previous = None
            current_position = 0
            while current is not None and current_position < position: # locates position of node to insert
                previous = current
                current = current.next
                current_position += 1

            # --- middle nodes --- #
            
            previous.next = new_node
            new_node.next = current
            new_node.next.prev = new_node
            current = new_node
            new_node.prev = previous
            
            if current is None: #tail 
                previous.next = new_node
                new_node.next = current # new node's next = None because tail
                current = new_node
                new_node.prev = previous
                self.tail = new_node

    def traversal(self):
        if not self.head:
            print('List is empty.')
        current = self.head
        print()
        while current:
            if current.next is None: # Prints tail
                print('[Prev Data:', current.prev.data, ' - Tail:', current.data, ' - Next:', current.next,']\n')
            elif current.prev is None: # Prints head
                print('[Prev Data:', current.prev, ' - Head:', current.data, ' - Next:', current.next.data,']')
            else: # Prints all middle nodes
                print('[Prev Data:', current.prev.data, ' - Node:', current.data, ' - Next:', current.next.data,']')
            current = current.next


linkedList = DoublyLinkedList()
linkedList.append([1, 2, 3])
linkedList.append({'a': 4, 'z': [1, 2, 3]})
linkedList.append(1)
linkedList.append('Hello')
linkedList.append(':)')
linkedList.delete(1) 
linkedList.insert(3, [1])
linkedList.traversal()


