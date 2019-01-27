import random,sys
sys.setrecursionlimit(10000)
l=list(range(1000))
random.shuffle(l)

def insert_sort(l):
    for i in range(1,len(l)):
        temp = l[i]
        j=i-1
        while j>=0 and temp<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=temp
insert_sort(l)
print(l)

random.shuffle(l)

def quick_sort(l,left,right):
    if left<right:
        mid=partition(l,left,right)
        quick_sort(l,left,mid-1)
        quick_sort(l,mid+1,right)

def partition(l,left,right):
    temp=l[left]
    while left <right:
        while left<right and temp>l[right]:
            right-=1
        l[left]=l[right]
        while left< right and temp<l[left]:
            left+=1
        l[right]=l[left]
    l[left]=temp
    return left

quick_sort(l,0,len(l)-1)
print(l)


random.shuffle(l)

def sipt(l,dad_node,last_node):
    left_child=dad_node*2+1
    temp=l[dad_node]
    while left_child<=last_node:
        if left_child+1<=last_node and l[left_child]<l[left_child+1]:
            left_child+=1
        if l[left_child]>temp:
            l[dad_node]=l[left_child]
            dad_node=left_child
            left_child=dad_node*2+1
        else:
            break
    l[dad_node]=temp



def heap_sort(l):
    n=len(l)
    for i in range(n//2-1,-1,-1):
        sipt(l,i,n-1)
    for i in range(n-1,-1,-1):
        l[0],l[i]=l[i],l[0]
        sipt(l,0,i-1)

heap_sort(l)
print(l)


















