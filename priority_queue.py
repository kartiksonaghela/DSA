class priorityqueue:
    def __init__(self):
        self.items=[]
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index=+1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            raise IndexError("queue is empty")
    def get_size(self):
        return len(self.items)

s1=priorityqueue()
s1.push(10,2)
s1.push("kartik",4)
print(s1.pop())