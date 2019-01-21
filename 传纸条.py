"""

XX 和 YY 经常在自习课的时候传纸条来传递一些私密性的信息。但是他们的座位相隔比较远，传纸条要通过其他人才能到达对方。在传递过程中，难免会有一些好奇心比较强的同学偷看纸条的内容。所以他们想到了一个办法，对纸条内容进行加密。

加密规则很简单：多次在信息的任意位置随意的添加两个相同的字母。

由于使用英文交流显得比较高端，所以他们的纸条内容只有英文。

现在给你加密后的信息，请你还原出原始的内容。

Input

输入数据的第一行为一个正整数 T(T ≤ 30)，表示共有 T 组测试数据。

接下来 T 行，每行为一个字符串，字符串仅包含小写英文字母，且保证原始字符串中不包含相邻两个相同的字母，字符串长度不超过200000。

Output


每组数据输出一行字符串，表示还原后的内容。

Sample Input

1
ssilofaafveuuu

Sample Output

iloveu
"""

num=int(input())
for i in range(num):
    s=input()
    u=[]
    for i in range(len(s)):
        if not len(u):
            u.append(s[i])
        elif u[-1]!=s[i]:
            u.append(s[i])
        elif u[-1]==s[i]:
            u.pop()
    result=''.join(u)
    print(result)










