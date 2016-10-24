# -*-coding:utf-8 -*-
#求100以内的素数
for i in range(2, 101):
	for j in range(2, i):
		if i % j == 0:
			break  # 用了一个break,执行到i%j==0时中断。
	else:
		print i,  # 原来要输出数字一行，加一个逗号就可以了。