# -*-coding:utf-8 -*-
L=[2,8,3,50]
G=[]
j=G.append(L)  # append和extend的区别 ，输出结果[[2, 8, 3, 50]]，append 接受的是一个对象
print G
j=[]
k=j.extend(L) # 输出结果[2, 8, 3, 50]  extend接受的是列表参数
print j   