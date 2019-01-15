"""

有N个石子，两人轮流取石子，良辰足够绅士所以让高数先取，每个人可以取至少1个至多K个石子，最先取完石子的人获胜，
大家知道的，良辰和高数两个人都是高智商人才，所以都足够的聪明。

Input

 多组输入。

对于每组数据有两个整数N，K（1 < = K < = N < = 1000），代表石子的数量和一次最多可取的石子的数量

Output


 对于每组数据，如果高数赢了，输出”mengmengda”，否则输出”hehe”（输出不包含引号，每组输出占一行）

Sample Input

5 3
8 3

Sample Output

mengmengda
hehe

"""
while True:
    try:
        n,m=(map(int,input().strip().split()))
        if n%(m+1):
            print('mengmengda')
        else:
            print('hehe')
    except Exception:
        break