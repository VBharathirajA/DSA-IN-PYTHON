


def bubble_sort(arr):
    print("Unsorted Array:",arr)
    for i in range(0, len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("Sorted Array:",arr)

        
arr=[65,9,3,8,543,2,1]
bubble_sort(arr)
