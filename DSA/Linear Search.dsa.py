import sys
ar=[1,2,3,4,5,6]

target = int(sys.argv[1])
print("Target Number:", target)

for i in range (0, len(ar)):
    if ar[i]==target:
        print("Element found at index:",i)
        break
else:
    print("Element Not found")
    
