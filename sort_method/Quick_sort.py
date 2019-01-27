import random
l=[233,456,2,11,56,3,43]

def quick_sort(l):
    if len(l)<2:
        return l
    else:
        temp=l[0]
        less=[i for i in l[1:] if i<=temp]
        more=[i for i in l[1:] if i>temp]
        return quick_sort(less)+[temp]+quick_sort(more)

result_l=quick_sort(l)
print(result_l)


def quick_sort1(l,left,right,isreverse=False):
    if left<right:
        mid=partition(l,left,right,isreverse)
        quick_sort1(l,mid+1,right,isreverse)
        quick_sort1(l,left,mid-1,isreverse)



def partition(l,left,right,isreverse):
    temp=l[left]
    if isreverse:
        while left<right:
            while left<right and l[right]<=temp:
                right-=1
            l[left]=l[right]
            while left<right and l[left]>=temp:
                left+=1
            l[right]=l[left]
        l[left]=temp
    else:
        while left<right:
            while left<right and l[right]>=temp:
                right-=1
            l[left]=l[right]
            while left<right and l[left]<=temp:
                left+=1
            l[right]=l[left]
        l[left]=temp
    return left

l1=list(range(10000))
random.shuffle(l1)
quick_sort1(l1,0,len(l1)-1,True)
print(l1)
