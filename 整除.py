'''
给你一个数字10000001（在两个1之间有n个0）（0 = < n < = 10000000）,判断这个数能不能被1001整除。
Input
多组输入，每组输入一个数字n.

Output
如果能整除1001，输出”Yes.”，否则输出”No.”。

Sample Input

2

Sample Output

Yes.

'''


while True:
    try:
        n = int(input())
        s = '1'
        for i in range(n):
            s += '0'
        s += '1'
        num = int(s)
        print(num)
        if not num % 1001:
            print('Yes.')
        else:
            print('No.')
    except:
        break



