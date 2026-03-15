class Node:
    def __init__ (self,data):
        self.data=data
        self.child=[]
       

class Tree:
    def __init__ (self):
        self.root=None

    def add(self,node,parent=None):
        newnode=Node(node)

        if not self.root:
            self.root=newnode
            return
        parentnode=self.find(self.root,parent)

        if not parentnode:
            print("Node not found")
            return
        parentnode.child.append(newnode)
        

    def find(self,node,parent):
            if node.data==parent:
                return node
            for i in node.child:
                node=self.find(i,parent)
                if node:
                    return node
            return None

    def display(self,root,level=0):
            
            if not root:
                print("Tree is empty")
                return

            print(" "*level,(root.data))

            for i in root.child:
                self.display(i,level+1)

    def remove(self,node):

        if self.root.data==node:
            self.root=None
            return
        parentnode=self.findparent(self.root,node)
        if not parentnode:
            print("Not found")
        for i in parentnode.child:
            if i.data==node:
                parentnode.child.remove(i)

    def findparent(self,root,node):

        for i in root.child:

            if i.data==node:
                return root
            newnode=self.findparent(i,node)
            if newnode:
                return newnode
        return None

    def height(self,node):

        if not node:
            return 0
        maxheight=0

        for i in node.child:

            h=self.height(i)
            maxheight=max(maxheight,h)
            
        return maxheight+1
            
            

t=Tree()
t.add(1)
t.add(2,1)
t.add(3,1)
t.add(4,2)
t.add(5,4)
t.add(6,1)
t.add(7,2)
t.display(t.root)



print()
print(t.height(t.root))

