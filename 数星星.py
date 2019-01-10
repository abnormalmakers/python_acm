"""

X晚上睡不着的时候不喜欢玩手机，也不喜欢打游戏，他喜欢数星星。

Input


 多组输入。

每组先输入一个整数N(N <= 10000)，接着输入两个点代表矩形的左下点B（x,y）和右上点T(x,y)，然后输入N个（X，Y）代表Ｎ颗星星。问有多少颗星星在窗子内部，在窗边上的不计。

Output


 输出一个整数，代表有多少颗星星在窗子内部。
3
0 1
3 4
1 1
2 2
3 3
2
1 1
5 5
4 4
0 6


Sample Output

1
1


e.g
3   1,3     2,3     3,3     3,4
2   1,2     2,2     2,3     2,3
1   1,1     1,2     1,3     1,4
0   1       2       3       4



思路：
    满足条件的星星：
        1.星星的横纵坐标大于左下点横纵坐标
        2.星星的横纵坐标小于右上点横纵坐标
"""

while True:
    starCount=int(input())
    if not starCount:
        break
    starIn=0
    lb_x,lb_y=map(int,input().strip().split())
    rt_x,rt_y=map(int,input().strip().split())
    for i in range(starCount):
        star_x,star_y=map(int,input().strip().split())
        if star_x>lb_x and star_x<rt_x and star_y>lb_y and star_y<rt_y:
            starIn+=1
    else:
        print(starIn)





