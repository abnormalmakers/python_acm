'''

验证“每个不小于6的偶数都是两个素数之和”，输入一个不小于6的偶数n，找出两个素数，使它们的和为n。

Input
输入一个不小于6的偶数n。

Output


找出两个素数，使它们的和为n。只需要输出其中第一个素数最小的一组数据即可。

Sample Input

80

Sample Output

80=7+73

'''

num=int(input())
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True

for i in range(3,num):
    if isPrime(i):
        a=num-i
        if isPrime(a):
            print('%d=%d+%d'%(num,i,a))
            break





