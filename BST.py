class Node:
    def __init__(self,left=None,right=None,item=None):
        self.left=left
        self.right=right
        self.item=item

class bst:
    def __init__(self):
        self.root=None
        self.item_count=0
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(item=Node)
        elif data<root.item:
            root.left=self.rinsert(root.left,data)
        else:
            root.right= self.rinsert(root.right,data)
        return root
    def search(self,data):
        return self.rseaerch(self.root,data)
    def rsearch(self,root,data):
        if root is None:
            return None
        elif root.item==data:
            return root
        elif root.item>data:
            return self.rsearch(root.right,data)
        else:
            return self.rsearch(root.right,data)
    def preorder(self):
        result=[]
        return self.rpreorder(self.root,result)
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    
    def postorder(self):
        result=[]
        return self.rpostorder(self.root,result)
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    
    def inorder(self):
        result=[]
        return self.rinorder(self.root,result)
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item
    def min_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return None
        if data < root.item:
            root.left=self.rdelete(root.left,data)
        elif data>root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.min_value(root.right)
            self.rdelete(root.right,root.item)
        return root
    def size(self):
        return len(self.inorder())