

def selection_sort(arr):
    for i in range (len(arr)-1):
        min=i
        for j in range (i+1, len(arr)):
            if arr[j]<arr[min]:
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)
            


arr=[8,7,6,5,4,54,34,12,3,4,1]             
selection_sort(arr)
