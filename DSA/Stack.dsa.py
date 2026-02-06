stack=[1,2,3,4,5,6,7,8]
print("Stack:",stack)

#Accessing 
print("Get Last Element in the stack",stack[-1])

#Insertion
stack.append(10)
print("Stack After Insert a element:",stack)

#Deletion
stack.pop()
print("Stack After Delete a Element:",stack)

#Searching

t=6
if t==stack[-1]:
    print("Last Element is Equal to Target Element")

