"""
列表被分为有序和无序两个区，最初有序区只有一个元素
每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空

"""
import random

l=list(range(1000))
random.shuffle(l)


def insert_sort(l):
    for i in range(1,len(l)):
        temp=l[i]
        j=i-1
        while j>=0 and temp<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=temp
    return l
l=insert_sort(l)
print(l)
