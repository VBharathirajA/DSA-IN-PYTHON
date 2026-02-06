import random
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    else:
        pivot=random.choice(arr)
    
        lef=[arr[i] for i in range(len(arr)) if arr[i]<pivot]
        rig=[arr[i] for i in range(len(arr)) if arr[i]>pivot]
        equ=[arr[i] for i in range(len(arr)) if arr[i]==pivot]
        
        return quick_sort(lef)+quick_sort(equ)+quick_sort(rig) 
        
       
arr=[8,7,6,5,4,3]
sort=quick_sort(arr)
print("Unsorted Array:",arr)
print("Sorted Array:",sort)
