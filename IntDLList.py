import IntDLLNode


class IntDLList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def prepend(self, value):
        new_node = IntDLLNode.IntDLLNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        print('Prepended {}!'.format(value))

    def append(self, value):
        new_node = IntDLLNode.IntDLLNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        print('Appended {}!'.format(value))

    def remove(self, value):
        if self.is_empty():
            print('Node not found')
            return
        node = self.head
        while node:
            if node.val == value:
                n = node.next
                p = node.prev

                if n:
                    n.prev = p
                else:
                    self.tail = p
                if p:
                    p.next = n
                else:
                    self.head = n

                self.size -= 1
                print('{} was removed from the list'.format(value))
                return
            else:
                node = node.next

        print('Node not found')

    def print_list(self):
        if self.is_empty():
            print('List is empty')
        else:
            node = self.head
            while node is not self.tail:
                print(node.val, end=', ')
                node = node.next
            print(node.val)
