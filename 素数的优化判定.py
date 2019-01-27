import math
import time
"""
1.朴素枚举法
"""
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if not n%i:
                return False
        else:
            return True

"""
2.缩小枚举范围，枚举到根号n
如果2到根号N范围不存在检测数字N的因子，则此数字N为素数
一个数字如果不是素数，那么他的两个因子都是成对出现（除去根号N）
例如:
    根号12=3.46.....
    12=3*4
    12=2*6
    其中一个因子一定小于根号N，
    所以如果2到根号N的范围内不存在数字N的因子，则N为素数
"""
def squrt_isPrime(n):
    sqrt_n=int(math.sqrt(n))
    if n<2:
        return False
    else:
        for i in range(2,sqrt_n+1):
            if not n%i:
                return False
        else:
            return True

#以上算法在大数据量时会超时

"""
我们继续分析，其实质数还有一个特点，就是它总是等于 6x-1 或者 6x+1，其中 x 是大于等于1的自然数。
如何论证这个结论呢，其实不难。首先 6x 肯定不是质数，
因为它能被 6 整除；其次 6x+2 肯定也不是质数，因为它还能被2整除；
依次类推，6x+3 肯定能被 3 整除；6x+4 肯定能被 2 整除。
那么，就只有 6x+1 和 6x+5 (即等同于6x-1) 可能是质数了。
所以循环的步长可以设为 6，然后每次只判断 6 两侧的数即可。
"""
import math
def six_isPrime(n):
    if n<2:
        return False
    elif n==2 or n==3:
        return True
    elif n==4:
        return False
    elif n%6!=1 and n%6!=5:
        return False
    else:
        num=int(math.sqrt(n))
        for i in range(5,num+1,6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True




"""

8600的手机每天消费1元，每消费K元就可以获赠1元，一开始8600有M元，问最多可以用多少天？

Input

 输入包括多个测试实例.每个测试实例包括2个整数M, k，（2 <= k <= M <= 1000).M = 0, k = 0代表输入结束.   	

Output

 对于每个测试实例输出一个整数，表示M元可以用的天数。   	

Sample Input

2 2
4 3
0 0

Sample Output

3
5

"""

while True:
    try:
        M,k=(map(int,input().strip().split()))
        day=0
        if not M and not k:
            break
        if not M:
            print(0)
            continue
        if M<k:
            print(M)
            continue
        else:
            while M:
                day += 1
                if day%k:
                    M-=1
            else:
                print(day)
    except:
        break




# price   day
# 5       0
# 4       1
# 4=3+1       2
# 3       3
# 3=2+1       4
# 2       5
# 2=1+1       6
# 1       7
# 1=0+1       8
# 0       9
# 5       0
# 4       1
# 3       2
# 3=2+1       3
# 2       4
# 1       5
# 1=0+1       6
# 0       7







