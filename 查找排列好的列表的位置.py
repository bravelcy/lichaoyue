#-*- coding:utf-8 -*-
def search(sequence,number,lower=0,upper=None):    # search() takes at least 3 arguments (2 given),漏写了lower=0,lower没有赋值
    if upper is None: upper=len(sequence)-1
    if lower==upper:
	   assert number==sequence[upper]
	   return upper
    else:
	   middle=(lower+upper)//2                       #另外一种除法是采用x//y的形式，那么这里采用的是所谓floor除法，即得到不大于结果的最大整数值，这个运算时与操作数无关的。比如2//3的结果是0，-2//3的结果是-1，-2.0//3的结果是-1.0。         
	      return search(sequence,number,middle+1,upper)
	   if number>sequence[middle]:                       
	      return search(sequence,number,middle+1,upper)
	   else:
	      return search(sequence,number,lower,middle)
seq=[34,67,8,123,4,100.95]
seq.sort()
print search(seq,2)                                     #2不在所给列表里面    错误为AssertionError，断言失败
