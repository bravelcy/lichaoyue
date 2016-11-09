# -*- coding:utf-8 -*-
def fab(n):
  if n<1:
     print ('输入出错！')  #斐波那契数列，迭代思想，好像比递归快
  
  
  if n==1 or n==2:
     return 1
  else:
     return fab(n-1)+fab(n-2)
result=fab(20)
if result !=-1:
    print u"总共生下的小兔崽子的数量%d"%result
