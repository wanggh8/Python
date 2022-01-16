'''
Author: your name
Date: 2021-04-23 15:11:47
LastEditTime: 2021-05-02 18:35:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Python/test1.py
'''
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equal', x, '*', n//x)
			break
	else:
		print(n, 'is a prime number')
		
def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end = ' ')
		a, b = b, a + b 
	print()	
fib(2000)	

a = 18
b = 7
print(a % b)