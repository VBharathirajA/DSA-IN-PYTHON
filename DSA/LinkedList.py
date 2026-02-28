class Node():

    def __init__(self,data):

        self.data=data
        self.next=None

class Link():

    def __init__(self):

        self.head=None
        self.tail=None

    def add(self,data):

        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:

            self.tail.next=newnode
            self.tail=newnode
    def addmiddle(self,data,pos):
        newnode=Node(data)
        count=1
        cur=self.head
        if pos==1:
            newnode.next=self.head
            self.head=newnode
            return
        
        while cur is not None and count<pos-1:
            cur=cur.next
            count+=1   
        newnode.next=cur.next
        cur.next=newnode     
        
    def display(self):

        cur=self.head
        while (cur is not None):
            print(cur.data)
            cur=cur.next
            
    def delete(self,node):
        cur=self.head
        if cur is not None:
            if cur.data==node:
                self.head=self.head.next
                return
            else:
                while cur.next is not None and cur.next.data!=node:
                    cur=cur.next
                    
        else:
            print("List is Empty")
        if cur.next is None:
            print("Value not found")
            return
        cur.next=cur.next.next

node=Link()
node.add(1)
node.add(2)
node.add(3)
node.add("John")
node.addmiddle(0,2)
print("After Adding Elements")
node.display()
rm="Johni"
node.delete(rm)
print("After remove:",rm)
node.display()
        

