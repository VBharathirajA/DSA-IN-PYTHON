
#Two sum using Two pointer algorithm

arr=[1,2,3,4,5,6,7,8,9]
target=7
lp=0
rp=len(arr)-1


while lp<rp:
    value=arr[lp]+arr[rp]
    if value==target:
        print("Left pointer:",lp,"\nRight pointer:",rp)
        break
    elif value>target:
        lp+=1
    else:
        value<target
        rp-=1
else:
    print("Not Found")
    
