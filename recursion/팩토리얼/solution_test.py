# 백준 10872번 팩토리얼 

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)
  
n = int(input())
print(factorial(n))