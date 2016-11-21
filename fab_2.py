# -*- coding:utf-8 -*-
def fab(n):      #斐波那契数列，用递归思想
   n1=1
   n2=1
   n3=1
   
	
   if n<1:
	 print('输入出错！')    
	 return -1
   while(n-2)>0:
	n3=n2+n1
	n1=n2            # IndentationError: unexpected indent,缩进错误，很多这样的问题
	n2=n3
	n-=1
	 
   return n3
result =fab(20)
if result !=-1:
   print u"总共生下的小兔崽子的数量%d"%result 
