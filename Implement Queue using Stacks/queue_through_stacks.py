class Node:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, item: int):
        new_node = Node(item, self.head)
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.val

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.head is None


class MyQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def add(self, x: int):
        self.stack_in.push(x)

    def _move_in_to_out(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def pop(self):
        self._move_in_to_out()
        return self.stack_out.pop()

    def peek(self):
        self._move_in_to_out()
        return self.stack_out.peek()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()
