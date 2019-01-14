# Problem Description
# 机械实验班有个同学叫小泉，有一天数学老师给小泉布置了一道个人作业，给小泉M（M<=100）组数据，每组数据有N个正整数（N<=100）让他把每组的N个数按升序排成一行，但由于数的数目比较多，人工做很费时，于是小泉就想到了喜欢编程序的你，请你帮他解决这个问题，可不要让他失望噢。
#
# Input
# 输入包括M+1行，第一行是两个正整数M、N；M表示总共多少组数据，下面M行每行包含N个正整数。（输入数据之间会用空格隔开）
# Output
# 输出包括M行，每行分别对应输入中M组数据的升序序列，数与数之间用一个空格隔开。
# Sample Input
# 2 3
# 1 3 2
# 4 2 6
#
# Sample Output
# 1 2 3
# 2 4 6

def choice_num(l):
    min_num=l[0]
    for i in range(1,len(l)):
        if min_num>l[i]:
            min_num=l[i]
    else:
        return min_num



def select_sort(l):
    arr=[]
    for i in range(len(l)):
        minum=choice_num(l)
        l.remove(minum)
        arr.append(minum)
    return arr

m,n=map(int,input().strip().split())
for i in range(m):
    iterable=map(int,input().strip().split())
    arr=[]
    while True:
        try:
            arr.append(next(iterable))
        except StopIteration:
            arr=select_sort(arr)
            break
    l=[str(x) for x in arr]
    s=' '.join(l)
    print(s)













