class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    
class dll:
    def __init__(self,start):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,value):
        n=Node(value,None,self.start)
        if self.is_empty() is not None:
            self.start.prev=n
        self.start=n
    def insert_at_end(self,value):
        if self.start is None:
            n=Node(value)
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=Node(value,temp,None)
            temp.next=n
    def search_node(self,data):
        if self.is_empty():
            pass
        else:
            temp=self.start
            while temp.next is not None:
                if temp.data==data:
                    return temp.data
                temp=temp.next
            return None
    def insert_after(self,temp,data):
        if self.is_empty():
            return None
        else:
            n=Node(data,temp.next,temp)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def print(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end='')
            temp=temp.next
        print()
    def delete_at_start(self):
        if self.is_empty():
            return
        elif self.start.next is None:
            self.start=None
        else:
            self.start=self.start.next
            self.start.prev=None
    def delete_at_end(self):
        if self.is_empty():
            return 
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None

    def delete_item(self,item):
        if self.is_empty():
            return
        if self.start.data==item:
            self.delete_at_start()
        else:
            temp=self.start
            while temp.next is not None:
                if temp.data==item:
                    if temp.next is None:
                        temp.prev.next=None
                    else:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                temp=temp.next

    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current
        self.current=self.currenr.next

##Single linked list
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Sll:
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
    def search_node(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not  None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return sllIterable(self.start)
class sllIterable:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data


mylist=Sll()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)

mylist.insert_after(mylist.search_node(20),50)
for x in mylist:
    print(x,end=' ')
print()
mylist.print_list()
print()
mylist.delete_item(20)
mylist.print_list()
mylist.delete_first()
print()
mylist.print_list()
mylist.delete_last()
print()
mylist.print_list()





            


