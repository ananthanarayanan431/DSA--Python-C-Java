
def QuickSort(mylist,low,up):
    if low<up:
        index=partition(mylist, low, up)
        QuickSort(mylist,low,index)
        QuickSort(mylist,index+1,up)



def partition(mylist,start,stop):
    pivot=mylist[start]
    left=start+1
    right=stop
    while True:
        while mylist[left]<pivot and left<right:
            left+=1
        while mylist[right]>pivot and right>=start:
            right-=1
        if left>=right:
            break
        mylist[left],mylist[right]=mylist[right],mylist[left]
    mylist[start],mylist[right]=mylist[right],mylist[start]
    return right

mylist = [6,2,9,7,4,8]
QuickSort(mylist,0,len(mylist)-1)
print(mylist)