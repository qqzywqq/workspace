增加背景音乐
触发背景音乐(单曲循环)
我方飞机诞生

interval = 0

while true:
    if 用户是否点击了关闭系统:
        游戏结束
    interval += 1
    if interval == 50:
      interval == 0
      小飞机诞生
    小飞机移动一个位置
    屏幕刷新
    if 用户鼠标改变位置:
        我方飞机中心位置=用户鼠标位置
        屏幕刷新
    if 我方飞机与小飞机发生肢体冲突:
        我方挂播放装机音乐
        修改我方飞机图案
        打印GameOver
        停止背景音乐最好淡出
