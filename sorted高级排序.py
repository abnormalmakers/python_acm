"""
给出n件物品，每件物品有质量和价格两种属性。你要做的是按质量升序排序，若质量相同则按价格降序排序。

Input

多组输入。每组先输入一个正整数n(1<=n && n <= 100)，代表有n件物品。接下来的一行有n个正整数Wi(1<= Wi && Wi <= 10000)，代表每件物品的质量。再接下来的一行有n个正整数Pi(1 <= Pi && Pi <= 10000)，代表每件物品的价格。

Output

对于每组数据输出n行，每行两个数Wi，Pi。顺序为题目描述所要求。

Sample Input

3
1 2 2
3 2 3

Sample Output

1 3
2 3
2 2

"""
while True:
    try:
        n=int(input())
        if not n:
            break
        m=list(map(int,input().strip().split()))
        p=list(map(int,input().strip().split()))
        l=[]
        for i,j in zip(m,p):
            l.append([i,j])
        l=sorted(l,key=lambda x:(x[0],-x[1]))
        s=''
        for i in range(len(l)):
            if i==len(l)-1:
                s+='%d %d'%(l[i][0],l[i][1])
            else:
                s += '%d %d\n' % (l[i][0], l[i][1])
        print(s)
    except Exception as e:
        break



