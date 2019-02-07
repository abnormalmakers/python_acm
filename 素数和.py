"""
NaYe 最近遇到了一个题，要求输出三个数，第三个数为前两个数的和，三个数都是素数，且前两个数小于 500000。他只需要输出任意一组符合要求的答案即认为是 Accepted。现在需要你做的是判断 NaYe 的程序运行结果对不对。

Input

输入数据有多组（数据组数不超过 100），到 EOF 结束。

对于每组数据，输入 a, b, c 三个整数。含义同题目描述。

a, b, c 均在 int 范围内。

Output

对于每组数据，如果 NaYe 的程序正确输出 “Accepted”，否则输出 “Wrong Answer”（输出不包括引号）。

Sample Input

1 1 1
2 3 5
3 5 8

Sample Output

Wrong Answer
Accepted
Wrong Answer
"""
import math
def isPrime(n):
    if n<2:
        return False
    elif n==2 or n==3:
        return True
    elif n%6!=1 and n%6!=5:
        return False
    else:
        num=int(math.sqrt(n))
        for i in range(5,num+1,6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True



while True:
    try:
        a, b, c = map(int, input().strip().split())
        if c != a + b:
            print('Wrong Answer')
        elif isPrime(a) and isPrime(b) and isPrime(c):
            print('Accepted')
        else:
            print('Wrong Answer')
    except:
        break


n=4
count=0

for i in range(n):
    count=(count+1)*2
print(count)