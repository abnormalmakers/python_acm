# Problem Description
#
# 根据输入的半径值，计算球的体积。
#
# Input
#
# 输入数据有多组，每组占一行，每行包括一个实数，表示球的半径。
#
# Output
#
# 输出对应的球的体积，对于每组输入数据，输出一行，计算结果保留三位小数。
#
# Sample Input
#
# 1
# 1.5
#
# Sample Output
#
# 4.189
# 14.137
import math

while True:
    try:
        r = input()
        if r == '':
            break
        r = float(r)
        v = 4 / 3 * 3.1415927 * math.pow(r, 3)
        v =float('%.3f' % v)
        print(v)
    except EOFError:
        break
