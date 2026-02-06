import array as ar

#Declare array
arr=ar.array('i',(1,2,3,4,5))

print ("Array is:",arr)
#Array Type
print("Array type:",type(arr),"\n")

#Insert Element
print("Insert 6 at 0th index")
arr.insert(0,6)
print(arr,"\n")

#Remove Element
print("Pop or remove a element")
arr.pop(0)
print(arr,"\n")

#Search Element
print("Search a element in a array")
target=5
for i in range(0, len(arr)):
    if arr[i]==target:
        print("Element found ar:",i)
        break
else:
    print("Element not found")
    



    
     
