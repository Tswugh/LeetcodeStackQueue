from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class FreqStack:
    def __init__(self):
        self.freq_stacks = deque()

    def push(self, val: int):
        current_freq = 0

        for head in self.freq_stacks:
            curr = head
            found = False
            while curr:
                if curr.val == val:
                    found = True
                    break
                curr = curr.next

            if found:
                current_freq += 1
            else:
                break

        new_node = Node(val)

        if current_freq == len(self.freq_stacks):
            self.freq_stacks.append(new_node)
        else:
            new_node.next = self.freq_stacks[current_freq]
            self.freq_stacks[current_freq] = new_node

    def pop(self):
        highest_level_head = self.freq_stacks[-1]

        popped_val = highest_level_head.val
        self.freq_stacks[-1] = highest_level_head.next
        if self.freq_stacks[-1] is None:
            self.freq_stacks.pop()

        return popped_val
