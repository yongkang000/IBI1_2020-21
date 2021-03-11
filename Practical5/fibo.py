def fibo(n): #define a function to make it clearer
  if n<=1:
    return n
  else:
    return fibo(n-1) + fibo(n-2) # make it back from n to 1
n=13
for i in range(1，n+1): #print from 1 to n result
  print(fibo(i))
