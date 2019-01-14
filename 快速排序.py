# Problem Description
#     给你N(N<=100)个数,请你按照从小到大的顺序输出。
# Input
#     输入数据第一行是一个正整数N,第二行有N个整数。
#
# Output
#     输出一行，从小到大输出这N个数，中间用空格隔开。
#
# Sample Input
#
# 5
# 1 4 3 2 5
#
# Sample Output
#
# 1 2 3 4 5


number_count=int(input())
num=map(int,input().strip().split())
arr=[]
for i in num:
    arr.append(i)

def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        item=arr[0]
        less_l=[x for x in arr[1:] if x<=item]
        more_l=[x for x in arr[1:] if x>item]
        return quick_sort(less_l)+[item]+quick_sort(more_l)


l=[str(x) for x in quick_sort(arr)]
s=' '.join(l)
print(s)







