"""
Problem Description


X最近爱上了一种奇怪的游戏，就是找出一个字符串中的最小循环节。

对于最小循环节的定义：对于字符串A存在字串B，使得A是由N个完整的B组成的，那么B就是A的一个循环节，长度最小的那一个为最小循环节。

Input


多组输入。

每组输入一个字符串，长度不大于80，只包含26个小写字母。

Output

输出一个字符串，代表最小循环节。

Sample Input

aaaa
abab

Sample Output

a
ab

"""
while True:
    try:
        s=input()
        if not s:
            break
        for i in range(1,len(s)):
            little_s=s[0:i]
            isfor=len(s)%len(little_s)
            if isfor:
                continue
            else:
                n=int(len(s)/len(little_s))
                news=''
                for i in range(n):
                    news+=little_s
                else:
                    if news!=s:
                        continue
                    else:
                        print(little_s)
                        break
        else:
            print(s)
    except:
        break
