def item_serach(l,item):
    low=0
    high=len(l)-1
    while low<=high:
        middle=(high+low) // 2
        print(middle,l[middle])
        if l[middle]>item:
            high=middle-1
        elif l[middle]<item:
            low=middle+1
        else:
            return middle
    return None

l=[1,2,3,4,5,6,7,8,9,10]
print(item_serach(l,5))


