
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            print("Target found at index:",mid)
            break
        elif arr[mid]>target:
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
    else:
        print("Element not found")
            
arr=[1,4,6,7,8,9,10,45,56,67,89]
binary_search(arr,45)
