# if...else语句   双分支
# score = 60
# if score<=60:
#     print('成绩不太好, 需要好好加油哦')
#     #pass   使用空语句也行, 有点麻烦哦
# #print('老师批语')
# else:
#     print('此次考试成绩还不错, 也要努力的')

#多分支, 多条件  考试成绩/猜拳
# score = int(input('请输入你本次考试成绩\n'))
# if score<= 60:
#     print('需要努力哦')
# elif score<=70:
#     print('成绩良')
#     pass
# elif score<=80:
#     print('成绩好')
# elif score<=90:
#     print('成绩优秀')
# else:
#     print('成绩很好啊')

# import random
# num = 0
# while num<10:
#     person_num = int(input('0:石头,1:剪刀,2:布\n'))
#     robot_num = random.randint(0, 2)
#     print(robot_num)
#     if person_num==1 and robot_num==2:
#         print('你赢了')
#     elif person_num ==2 and robot_num==0:
#         print('你赢了')
#     elif person_num==0 and robot_num ==1:
#         print('你赢了')
#     elif person_num==robot_num:
#         print('打平了')
#     else:
#         print('你输了')
#     num+=1
#     if num == 9:
#         print('游戏结束')

# 案例: 输出1-100之间的数字
# num =1
# while num <=100:
#     print(num)
#     num+=1

# 打印九九乘法表  页面合成展示
# row = 1 #行
# while row <10:
#     col = 1  # 列, 每行列都是从1开始
#     while col<=row:
#         #列*行=列*行
#         print('%d*%d=%d'%(col,row,col*row),end=' ')  #使用end ,不换行
#         col+=1
#         pass
#     row+=1
#     #换行
#     print() #print 默认换行
#     pass

#打印直角三角形
row=1
while row<=10:
    col = 1
    while col<=row:
        print('.',end =' ')
        col+=1
        pass
    row+=1
    print('')  #换行
    pass
#打印等腰三角形