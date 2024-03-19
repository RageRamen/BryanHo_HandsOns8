class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return len(self.data) == self.max_size

    def push(self, value):
        if not self.is_full():
            self.data.append(value)
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            print("Stack Underflow")
            return None


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return len(self.data) == self.max_size

    def enqueue(self, value):
        if not self.is_full():
            self.data.append(value)
        else:
            print("Queue Overflow")

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            print("Queue Underflow")
            return None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:

# Stack
stack = Stack(6)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print("Stack:")
while not stack.is_empty():
    print(stack.pop(), end=" ")
print()

# Queue
queue = Queue(6)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print("Queue:")
while not queue.is_empty():
    print(queue.dequeue(), end=" ")
print()

# Singly Linked List
linked_list = SinglyLinkedList()
linked_list.insert_at_start(1)
linked_list.insert_at_start(2)
linked_list.insert_at_start(3)
linked_list.insert_at_start(4)
linked_list.insert_at_start(5)
linked_list.insert_at_start(6)
print("Linked List:")
linked_list.display()
