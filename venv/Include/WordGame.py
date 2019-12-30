# 这是个文字小游戏
import random

secret = random.randint(1,10)
print('---------这是一个猜测数字的小游戏---------')
temp = input("不妨猜一下我现在心里想的是哪个数字:")
guess = int(temp)
intstr = 0
while guess != secret and intstr !=2:
    if guess == secret:
        print("卧槽,你是我心中的蛀虫吗？！")
        print("哼！猜中了也没奖励!")
    else:
        if guess > secret:
            print("哥！大了 大了")
        else:
            print("嘿 小了 小了")
    temp = input("哎呀猜错了,请重新猜测吧:")
    guess= int(temp)
    if guess == secret:
        print("卧槽,你是我心中的蛀虫吗？！")
        print("哼！猜中了也没奖励!")
    else:
        if guess > secret :
            print("哥！大了 大了" )
        else :
            print("嘿 小了 小了" )
    intstr = intstr + 1
if intstr == 2 and guess != secret:
    print("你已经猜错三次了！不玩啦^_^")
else :
    if intstr == 0:
        print("上来就猜测中了，不玩了不玩了")
    else :
        print("哎呀呀！不玩了不玩了")


