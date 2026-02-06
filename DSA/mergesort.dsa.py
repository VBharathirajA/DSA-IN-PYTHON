def merge_sort(arr):
    #Divide until sub array contain one element
    if len(arr)>1:
        mid=len(arr)//2
        lef_arr=arr[:mid]
        right_arr=arr[mid:]


        merge_sort(lef_arr)
        merge_sort(right_arr)

        #Sort the sub array elements 
        lp=0
        rp=0
        fp=0

        while (lp < len(lef_arr) and rp < len(right_arr)):
            if lef_arr[lp]<right_arr[rp]:
                arr[fp]=lef_arr[lp]
                lp+=1
            else:
                arr[fp]=right_arr[rp]
                rp+=1
            fp+=1

        #Merge the sorted sub array

        while lp<len(lef_arr):
            arr[fp]=lef_arr[lp]
            fp+=1
            lp+=1
                

        while rp<len(right_arr):
            arr[fp]=right_arr[rp]
            fp+=1
            rp+=1

        return arr

arr=[8,6,5,4,78,3,1]
print("Unsorted Array:",arr)
merge_sort(arr)
print("Sorted Array:",arr)
