"""
Input


输入数据有多组（数据组数不超过 100），到 EOF 结束。

每组数据输入一行长度不超过 1000 的字符串。

Output
如果字符串中包含至少一段连续的 "gaoshu"，输出 "Good job!!!"，否则输出 "QAQ"（不包含引号）。

Sample Input

gaoshu
ACM International Collegiate Programming Contest
Probability Theory The Logic of Science
I love gaoshu (are you kidding me?)
gao liang shu le

Sample Output

Good job!!!
QAQ
QAQ
Good job!!!
QAQ

"""

while True:
    try:
        s=input()
        if not s:
            break
        result=s.find('gaoshu')
        if result!=-1:
            print('Good job!!!')
        else:
            print('QAQ')
    except Exception:
        break





