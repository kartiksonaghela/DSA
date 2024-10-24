class stack:
    def __init__(self):
        self.list=[]
    def is_empty(self):
        return len(self.list)==0
    def push(self,data):
        return self.list.append(data)
    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        return self.list[-1]
    def size(self):
        if not self.is_empty():
            return len(self.list)
        else:
            raise IndexError("Stack is empty")
