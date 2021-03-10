def fibo(n):
  if n<=1:
    return n
  else:
    return fibo(n-1) + fibo(n-2)
n=13
for i in range(1，n+1):
  print(fibo(i))
