"""

在一个果园里，多多已经将所有的果子打了下来，而且按果子的不同种类分成了不同的堆。多多决定把所有的果子合成一堆。
每一次合并，多多可以把两堆果子合并到一起，消耗的体力等于两堆果子的重量之和。可以看出，所有的果子经过n-1次合并之后，就只剩下一堆了。多多在合并果子时总共消耗的体力等于每次合并所消耗体力之和。

因为还要花大力气把这些果子搬回家，所以多多在合并果子时要尽可能地节省体力。假定每个果子重量都为1，并且已知果子的种类数和每种果子的数目，你的任务是设计出合并的次序方案，使多多耗费的体力最少，并输出这个最小的体力耗费值。

例如有3种果子，数目依次为1，2，9。可以先将1、2堆合并，新堆数目为3，耗费体力为3。接着，将新堆与原先的第三堆合并，又得到新的堆，数目为12，耗费体力为12。所以多多总共耗费体力=3+12=15。可以证明15为最小的体力耗费值。



Input

 第一行是一个整数n(1<=n<=10000),表示果子的种类数。第二行包含n个整数，用空格分隔，第i个ai(1<=ai<=20000)是第i个果子的数目。


Output

 输出包括一行，这一行只包含一个整数，也就是最小的体力耗费值。输入数据保证这个值小于2^31。


Sample Input

3
1 2 9

Sample Output

15

"""

l=[1,2,9,5,7]

"""
    12
9       3
    2       1
1+2+3+9=15

        24
     9     15
        7       8
            5       3
                2       1

1+2+3+5+8+7+15+9=50

        24
     5     19
        7       12
            9       3 c sums
                2       1

1+2+3+9+12+7+19+5=58
6 15 27 34 53 58

35
    26
8       18
    7       11
        6        5
            1       4
1+4+6+5+7+11+8+18

"""
n=int(input())
l=list(map(int,input().strip().split()))

def sipt(l,dad_node,last_node):
    left_child = dad_node * 2 + 1
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

def main(l):
    if len(l)<3:
        return sum(l)
    else:
        c=l[0]+l[1]
        sums=c
        for i in range(2,len(l)):
            c+=l[i]
            sums+=c
        return sums
result=main(l)
print(result)


















