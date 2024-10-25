class queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,value):
        self.items.append(value)
        #self.rear=+1
    def dequeue(self):
        self.items.pop(0)
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")
    def get_size(self):
        return len(self.items)

q1=queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
print(q1.get_front(),q1.get_rear())
q1.enqueue(30)
print(q1.get_front(),q1.get_rear())
q1.enqueue(40)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())
print(q1.get_size())
