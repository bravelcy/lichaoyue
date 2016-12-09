# -*- coding:utf-8 -*-
def hanoi(n,x,y,z):
   if n==1:
        print x,'-->',z
   else: 
	  hanoi(n-1,x,z,y)#将n-1个盘子从x移动到y上
	  print 'a'
	  print x,'-->',z #将最后一个盘子从x移动到z上
	  print 'b'
	  hanoi(n-1,y,x,z)#将n-1个盘子从y移动到z上
print u"输入总层数："
n=int(input('>'))
hanoi(n,'X','Y','Z') 

#中间输入的print 'a'和print 'b'是为了看程序运行过程
#先研究hanoi(3)的过程，先传输参数hanoi(3,'X','Y','Z')给形参，此时n=3，跳到else
#分三个分支1.hanoi(2,X,Z,Y)  2.X-->Y   3.hanoi(2,Y,X,Z)，先判断1的情况，要调用函数，if条件到esle这，又分三个分支，依次判断