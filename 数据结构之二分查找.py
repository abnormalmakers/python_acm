"""

在一个给定的无重复元素的递增序列里，查找与给定关键字相同的元素，若存在则输出找到的位置,不存在输出-1。

Input


一组输入数据，输入数据第一行首先输入两个正整数n ( n < = 10^6 )和m ( m < = 10^4 )，
n是数组中数据元素个数，随后连续输入n个正整数，输入的数据保证数列递增。
 随后m行输入m个待查找的关键字key

Output


若在给定的序列中能够找到与关键字key相等的元素，则输出位序(序号从0开始)，否则输出-1。

Sample Input

8 3
4 6 8 9 13 20 21 22
6
8
17

Sample Output

1
2
-1

"""



n,m=(int(i) for i in input().strip().split())
l=[x for x in map(int,input().strip().split())]
print(len(l))
# def item_search(l):
#     max_num = len(l) - 1
#     min_num = 0
#     search_num = int(input())
#     while min_num<=max_num:
#         item = (max_num+min_num) // 2
#         if search_num<l[item]:
#             max_num=item-1
#         elif search_num>l[item]:
#             min_num=item+1
#         elif search_num==l[item]:
#             print(item-1)
#             break
#     else:
#         print(-1)
#     return None
def binary_search(alist, item):
    """二分查找,递归"""
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return mid
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return -1


for i in range(m):
    item=int(input())
    result=binary_search(l,item)
    print(result)







