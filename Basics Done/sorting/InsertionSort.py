
def InsertionSort(mylist):
    for i in range(1,len(mylist)):
        key=mylist[i]
        j=i-1
        while j>=0 and key<mylist[j]:
            mylist[j+1]=mylist[j]
            j-=1
        mylist[j+1]=key
    return mylist

print(InsertionSort([7,3,4,5,1]))