class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start 
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n

    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def deletion_at_start(self):
        if self.start is not None:
            self.start=self.start.next
    def deletion_at_last(self):
        
        if self.start.next is None:
           self.start=None
        elif self.start is None:
            pass
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next) 
            temp.next = n  

    def search_node(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp.item
            temp=temp.next
        return None
    def delete_item(self,data):
        if self.is_empty():
            return None
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None  
        
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            while temp.next is not None:
                if temp.next.item ==data:
                    temp.next=temp.next.next
                    break
                temp=temp.next
