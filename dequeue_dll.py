class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
class Dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front==None
    def insert_front(self,data):
        n=Node(data,prev=None,next=self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n        
        self.item_count+=1    
    def insert_rear(self,data):
        n=Node(data,prev=self.rear,next=None)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n 
        self.item_count+=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("dequeue is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("dequeue is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("dequeue is empty")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("dequeue is empty")
        else:
            return self.rear.item
    def get_size(self):
        return self.item_count
# Create a dequeue instance
dq = Dequeue()

# Test inserting elements at the front
dq.insert_front(10)
dq.insert_front(20)
print("Front after inserting 20 and 10 at front:", dq.get_front())  # Should print 20
print("Rear after inserting 20 and 10 at front:", dq.get_rear())    # Should print 10
print("Size after inserting 20 and 10 at front:", dq.get_size())    # Should print 2

# Test inserting elements at the rear
dq.insert_rear(30)
dq.insert_rear(40)
print("Front after inserting 30 and 40 at rear:", dq.get_front())   # Should print 20
print("Rear after inserting 30 and 40 at rear:", dq.get_rear())     # Should print 40
print("Size after inserting 30 and 40 at rear:", dq.get_size())     # Should print 4

# Test deleting from the front
dq.delete_front()
print("Front after deleting one element from front:", dq.get_front()) # Should print 10
print("Size after deleting one element from front:", dq.get_size())   # Should print 3

# Test deleting from the rear
dq.delete_rear()
print("Rear after deleting one element from rear:", dq.get_rear())     # Should print 30
print("Size after deleting one element from rear:", dq.get_size())     # Should print 2

# Edge case: Deleting all elements
dq.delete_front()
dq.delete_rear()
print("Is empty after deleting all elements:", dq.is_empty())          # Should print True
print("Size after deleting all elements:", dq.get_size())              # Should print 0

# Edge case: Trying to delete from an empty dequeue should raise an error
try:
    dq.delete_front()
except IndexError as e:
    print("Error:", e)  # Should print "dequeue is empty"
