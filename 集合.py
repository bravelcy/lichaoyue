# -*- coding: utf-8 -*-

num1={1,2,3,4,5,5,4,3,2,1,0}  #集合里面的数是唯一的
num3={11,12,13}
print num1                  #打印出来的数就是去掉了重复的
# for in 和for not in 
num1.add(8)                   #add为添加元素到集合里面，发现只能添加一个元素
print num1
num1.update(num3)              #update 将一个字典添加到另一个字典里面
print num1

temp=[]
for each in num1:              #去掉重复元素
    if each not in temp:
	     temp.append(each)
print temp

num1=list(set(num1))             #直接返回集合元素，再形成列表
print num1

num1.remove(4)                   #去掉指定元素
print num1

num2=frozenset(num1)             #冰冻，不可变集合
print num2
num2.remove(5)                  #AttributeError: 'frozenset' object has no attribute 'remove',报错，不能删除
print num2



