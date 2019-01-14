"""

白具有超强的记忆力和数学推演能力，在与世上最强国际象棋程序交换先后手的较量中，获得了 20 连胜的成绩。
其原因其实是她超强的大脑心算能力，并且是并行的。也就是说她可以一次处理多个事件。现在给你 n 个事件和她最多能一次处理的事件数 m。
然后每个事件都会有 num 个步数，每处理一个步数就需要花费 1 分钟（1 分钟只能处理 1 个事件的 1 个步骤，但可以同时处理 m 个不同的事件）。
现在你来计算一下她最少需要多少分钟处理完这 n 个事件。

Input


输入数据有多组（数据组数不超过 20），到 EOF 结束。

对于每组数据：
•第一行包含两个以空格分隔开的正整数 n, m (1 <= n, m <= 40000）。
•第二行包含 n 个数，表示每个事件需要处理的步数。每个数介于 1~40000 之间。

Output


对于每组数据，输出一个整数，表示她完成这 n 个事件需要的最少分钟数。

Sample Input

3 2
2 2 2
10 6
1 2 3 4 5 6 7 8 9 10

Sample Output

3
10
"""
"""
思路：每次选步骤做多的m个事件
    1 2 3 4 5 6 7 8 9 10
1           4 5 6 7 8 9
2           3 4 5 6 7 8
3           2 3 4 5 6 7
4           1 2 3 4 5 6
5           0 1 2 3 4 6
6         3   0 1 2 3 4
7       2 2     0 1 2 3
8     1 1 1       0 1 2
9   0 0 0 0         0 1
10                    0

9 5
2 4 3 4 3   sum=19
            avg=19/5

wrong
1   0 1 2 3 4 5
2     0 1 2 3 4 6
3       0 1 2 3 5 7
4         0 1 2 4 6 8
5           0 1 3 5 7 9
6             0 2 4 6 8
7


6  2
    2 3 1 3 5 7
1           4 6
2           3 5
3     2       4
4         2   3
5           2 2
6   1 1
7         1 1
8   0         1
9     0 0
10        0 0
11             0      
"""

#方法1
# def chioce_max_m(l, m):
#     newarr = []
#     for i in range(m):
#         max_now = max(l)
#         newarr.append(max_now - 1)
#         l.remove(max_now)
#     return newarr
#
# while True:
#     try:
#         n,m=map(int,input().strip().split())
#         sum_time=0
#         things=[int(x) for x in list(map(int,input().strip().split()))]
#         while sum(things):
#             if n<=m:
#                 sum_time=max(things)
#                 break
#             else:
#                 zero_num = things.count(0)
#                 if len(things) - zero_num <= m:
#                     sum_time+=max(things)
#                     break
#                 arr=chioce_max_m(things,m)
#                 things.extend(arr)
#                 sum_time+=1
#         print(sum_time)
#     except Exception:
#         break

# 方法2
while True:
    try:
        n, m = map(int, input().strip().split())
        sum_time = 0
        things=[int(x) for x in list(map(int,input().strip().split()))]
        sum_step=sum(things)
        max_n=max(things)
        avm=sum_step/m
        if sum_step%m:
            avm+=1
        max_n=int(max([max_n,avm]))
        print(max_n)
    except Exception:
        break