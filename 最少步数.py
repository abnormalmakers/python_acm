"""
给定一个数字n，我们可以进行3种操作，加1，减1，如果可以整除2，还可以除2，问最少多少步变换到1.

Input

 输入数据的第一行包含数字n(1<=n<=10000000)。多组输入。

Output

 计算结果。

Sample Input

3

Sample Output

2
"""
# 错误答案  例：输入167
# while True:
#     try:
#         num=int(input())
#         if not num:
#             break
#         count=0
#         while num!=1:
#             if num>1 and num%2:
#                 num-=1
#                 count+=1
#             elif not num%2:
#                 num/=2
#                 count+=1
#         print(count)
#     except:
#         break


def set_count(num):
    count=0
    if num==1:
        count=0
        return count
    if num==2:
        count=1
        return count
    else:
        if num%2==0:
            count=set_count(num/2)+1
        else:
            count=set_count(num+1)+1 if set_count(num-1)>set_count(num+1) else set_count(num-1)+1
        return count
while True:
    try:
        num=int(input())
        k=set_count(num)
        print(k)
    except Exception:
        break

167
166
83
82
41
40
20
10
5
4
2
1

167
168
84
42
21
20
10
5
4
2
1
