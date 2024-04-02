def linearsearch(unordered_list,key):
    for i in range(len(unordered_list)):
        if unordered_list[i]==key:
            return True
    return False

print(linearsearch([14,2,21,3,12,7,8],8))