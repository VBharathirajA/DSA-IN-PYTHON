class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Link():
    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,data):

        newnode=Node(data)
        cur=self.head

        if cur is None:
            self.head=newnode
            self.tail=newnode
            return
        else:
            self.tail.next=newnode
            
            newnode.prev=self.tail
            self.tail=newnode


    def addmiddle(self,data,pos):
        newnode=Node(data)
        cur=self.head
        count=1
        if pos==1:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
        else:
            while cur is not None and count<pos-1:
                cur=cur.next
                count+=1
        newnode.next=cur.next
        newnode.prev=cur
        cur.next.prev=newnode
        cur.next=newnode
    def delete(self,node):
        cur=self.head
        if (cur is not None):
            if cur.data==node:
                self.head=self.head.next
                self.head.prev=None
                return
            else:
                while cur.next is not None and cur.next.data!=node:
                    cur=cur.next
        else:
            print("List is Empty")
        if cur.next is None:
            print("Value is not found")
            return

        cur.next=cur.next.next
        cur.next.prev=cur
             
            
            
    def display(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next


    def displayback(self):
        cur=self.head
        while cur.next is not None:
            cur=cur.next

        while cur is not None:
            print(cur.data)
            cur=cur.prev




li=Link()
li.add(1)
li.add(2)
li.add(3)
li.add(4)
li.add(5)
li.addmiddle(0,2)
print("After Adding Nodes in the List")
li.display()
rm=2
li.delete(rm)
print("After remove:",rm)
li.display()
print("Reverse the List")
li.displayback()
