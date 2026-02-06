ar=[1,2,3,4,5,6]

target=int(input("Enter Target Number:"))

for i in range (0, len(ar)):
    if ar[i]==target:
        print("Element found at index:",i)
        break
else:
    print("Element Not found")
    
