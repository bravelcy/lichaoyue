#-*- coding:utf-8 -*-
def search(sequence,number,lower=0,upper=None):    # search() takes at least 3 arguments (2 given),漏写了lower=0,lower没有赋值
    if upper is None: upper=len(sequence)-1
    if lower==upper:
	   assert number==sequence[upper]
	   return upper
    else:
	   middle=(lower+upper)//2                       #python 2.x里面，// 是地板除，/如果有一个数是浮点数就得到小数，如果两个都是整数也是地板除。
	   if number>sequence[middle]:
	      return search(sequence,number,middle+1,upper)
	   else:
	      return search(sequence,number,lower,middle)
seq=[34,67,8,123,4,100.95]
seq.sort()
print search(seq,2)                                     #2不在所给列表里面    错误为AssertionError，断言失败
