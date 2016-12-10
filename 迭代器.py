#-*- coding:utf-8 -*-
class Fibs:
        def  __init__(self):
               self.a=0
               self.b=1
        def next(self):
               self.a,self.b=self.b,self.a+self.b  
               return self.a
        def __iter__(self):      #迭代器协议是指：对象需要提供next方法，它要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代
               return self               #迭代器返回的是自身，一直重复next()的方法

fibs=Fibs()
for f in fibs:                           #fibs是迭代器中生成的一个列表
    if f<1000:
        print f               
    else: 
        break

#借用一个人说的，非要类比的话，赌场发牌的荷官算是一个比较接近的例子。本来你需要自己去处理一堆牌（一个 collection），现在你有了这个对象，只要不断问他要“下一张”，他要是有自然会给你，没有就结束（StopIteration）