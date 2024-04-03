
def bubble_sort(mylist):
    list_length=len(mylist)
    for i in range(list_length-1):
        for j in range(list_length-1-i):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
    return mylist

def BubbleSort(mylist):
    list_length=len(mylist)
    is_sorted=False
    while not is_sorted:
        is_sorted=True
        for i in range(list_length-1):
            if mylist[i]>mylist[i+1]:
                mylist[i],mylist[i+1]=mylist[i+1],mylist[i]
                is_sorted=False
        list_length-=1
    return mylist

print(BubbleSort([4,3,7,1,5]))