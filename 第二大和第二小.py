"""
Problem Description


对于一个数组，次大的数指数组中第二大的数，相似地，次小的数指数组中第二小的数。

给定一个含有 n 个数的数组（数组中的数互不相同），求其中次大的数和次小的数。

Input


首先输入一个整数 T (1 <= T <= 200)，表示数据组数。

对于每组数据：
•第 1 行输入一个整数 n (2 <= n <= 1000)，表示数组中元素的数量。
•第 2 行输入 n 个用空格隔开的整数 Ai (-10000 <= Ai <= 10000)，表示数组中每一个元素的值。

Output


对于每组数据，输出一行，包含 2 个整数 a, b，分别表示次大和次小的数。

Sample Input

1
5
3 1 2 4 5

Sample Output

4 2

"""

# num=int(input())
# for i in range(num):
#     try:
#         l_count=int(input())
#         l=list(map(int,input().strip().split()))
#         # for i in range(l_count):
#         #     num=int(input())
#         max_num=max(l)
#         min_num=min(l)
#         l.remove(max_num)
#         l.remove(min_num)
#         new_max=max(l)
#         new_min=min(l)
#         print(new_max,new_min)
#     except:
#         break

import math
def isPrime(n):
    num=int(math.sqrt(n))
    if n<2:
        return False
    else:
        for i in range(2,num+1):
            print("n:", n, "num:", num)
            if not n%i:
                return False
        else:
            return True

n=int(input())
count=0

for i in range(2,n+1):
    papa=isPrime(i)
    if papa:
        count+=1
else:
    print(count)