

def selectionSort(mylist):
    listlength=len(mylist)
    for i in range(listlength-1):
        lowest=mylist[i]
        index=i
        for j in range(i+1,listlength):
            if mylist[j]<lowest:
                lowest=mylist[j]
                index=j
        mylist[i],mylist[index]=mylist[index],mylist[i]
    return mylist

print(selectionSort([7,4,5,3,1]))
