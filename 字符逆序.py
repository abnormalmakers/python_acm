# 将一个字符串str的内容颠倒过来，并输出。str的长度不超过100个字符。
#
# Input
#
# 输入包括一行。
#  第一行输入的字符串。
#
# Output
#
# 输出转换好的逆序字符串。
#
# Sample Input
#
# I am a student
#
# Sample Output
#
# tneduts a ma I

a=input()
l=list(a)
l.reverse()
s=''.join(l)
print(s)

