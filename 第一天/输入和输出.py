'''多行注释, 输入和输入联系'''
print('我叫红儿,我来自湖北')
#占位符 %代替
#name = '陈林'
name = input('输入姓名')
home = '黄冈'
age = 30
# print('姓名%s'%name)
# print('我的名字是%s,我的家乡是%s,我的年龄是%d岁'%(name,home,age))
# print('我的家\n你的家')
#格式输出的其他方式:     .format()
print('姓名是{},爱人是{}'.format(name,'志红'))
print('家乡:{}'.format(home))
print('年龄:{}'.format(age))
print(type(2))