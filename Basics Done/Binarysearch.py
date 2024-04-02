
def binearSeach(ordered_list,key):
    first = 0
    last = len(ordered_list)-1
    while first<=last:
        mid = (first+last)//2
        if ordered_list[mid]==key:
            return True
        elif ordered_list[mid]>key:
            last=mid-1
        else:
            first=mid+1
    return False

print(binearSeach([2,5,10,12,15,17,20],15))