class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("No data present")
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data present")
        else:
            return self.rear.item

    def size(self):
        return self.count

q = Queue()

# Test is_empty on an empty queue
print("Is queue empty?", q.is_empty())  # Expected: True

# Test enqueue operation
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Test is_empty after enqueues
print("Is queue empty?", q.is_empty())  # Expected: False

# Test get_front and get_rear
print("Front item:", q.get_front())  # Expected: 10
print("Rear item:", q.get_rear())    # Expected: 30

# Test size of queue
print("Queue size:", q.size())       # Expected: 3

# Test dequeue operation
print("Dequeued item:", q.dequeue())  # Expected: 10

# Check front and size after dequeue
print("Front item after dequeue:", q.get_front())  # Expected: 20
print("Queue size after dequeue:", q.size())       # Expected: 2

# Test dequeue until empty
q.dequeue()  # Removes 20
q.dequeue()  # Removes 30

# Test is_empty after dequeues
print("Is queue empty?", q.is_empty())  # Expected: True

# Try to dequeue from an empty queue (should raise an error)
try:
    q.dequeue()
except IndexError as e:
    print(e)  # Expected: "Empty Queue"
