#coding=utf-8
#author：zhujingyuan
def score():
    points=float(raw_input(u'请输入您的成绩：\n'))
    if points>=90:
        print '成绩是{0},等级是A'.format(points)
    elif points>=60 and points<89:
        print '成绩是{0},等级是B'.format(points)
    else :
        print '成绩是{0},等级是C'.format(points)
# score()


def game():

    count = 1
    while (count<=3):
        num = int(raw_input(u'请输入您要输入的数字\n'))
        if num==10:
            print '恭喜你，答对了'
        elif num!=10:
            print '输入错误'
        count=count+1
    print '游戏结束'
game()
test zhujingyuan

# count = 1
# for i in range(1,5):
#     for m in range(1,5):
#         for n in range(1,5):
#             if ((i!=m) and (m!=n) and (n!=i)):
#                 print (m,i,n)
#                 count +=1
# print(count)




import os
import time

