
#要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”

temp = input("请在1到100之中输入一个数字:")

guss = int(temp)

if guss>0 :
    if guss <101:
        print("你妹好漂亮")
    else:
        print("你大爷好丑")
else:
    print("你大爷好丑")