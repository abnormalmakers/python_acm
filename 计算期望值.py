#
# 众所周知，标标是机械学院的，在大二的会有一段时间去实习，称之为金（无）工（聊）实习，但是标标还要做训练和参加EC-Final比赛，
# 所以标标对于一些不感兴趣的实习决定要逃课，可是逃课的话就只能得到60分，不逃课就可以得到90分，标标想知道他能期望得到的分数是多少。
#
# Input
#
#
# 多组输入，每组一个整数n(0 < n < = 100),表示实习的工种的个数，接下来n个数表示对应工种标标逃课的概率。
#
# Output
#
#
# 输出期望分数。结果保两位小数。
#
# Sample Input
#
# 2
# 0.5 0.5
#
# Sample Output
#
# 150.00


while True:
    class_num = input()
    if not class_num:
        break
    class_num=int(class_num)
    probablity=list(map(float,input().strip().split()))
    def point():
        p=0
        for i in probablity:
            num=60*i+90*(1-i)
            p+=num
        print('%.2f'%p)
    point()
