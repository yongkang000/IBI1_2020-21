mima =input('请设置密码（6位数）')
for i in range(0,1000000):
  if i == int(mima):
    break
if i==0:
  print('破解结果：你的密码是：'+'000000')
else:
  n=0
  while i<1000000:
    n+=1
    i*=10
  m=0
  for x in range(n):
    i= i/10
  print( '破解结果：你的密码是：' +'0'*(n-1)+ str(int(i)) )
