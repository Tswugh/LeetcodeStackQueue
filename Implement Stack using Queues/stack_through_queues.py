class Node:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, item: int):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty queue")

        popped_value = self.head.val
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.head.val

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0


class MyStack:
    def __init__(self):
        self.q = Queue()

    def push(self, x: int):
        self.q.add(x)
        for _ in range(self.q.size() - 1):
            self.q.add(self.q.pop())

    def pop(self):
        return self.q.pop()

    def top(self):
        return self.q.peek()

    def empty(self):
        return self.q.is_empty()
