


def merge_sort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        left=mylist[:mid]
        right=mylist[mid:]
        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                mylist[k]=left[i]
                i+=1
            else:
                mylist[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            mylist[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            mylist[k]=right[j]
            j+=1
            k+=1

mylist=[35,22,90,4,50,20,30,40,1]
merge_sort(mylist)
print(mylist)