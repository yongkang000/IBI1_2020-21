password =input('plesae set your password with 6 number')
for i in range(0,1000000):
  if i == int(password):
    break
if i==0:
  print('The result：your password is'+'000000')
else:
  n=0
  while i<1000000:
    n+=1
    i*=10
  m=0
  for x in range(n):
    i= i/10
  print( 'The result：your password is' +'0'*(n-1)+ str(int(i)) )
