a= 140702
b= 190784
c= 100321
d= a-c
e= b-c
if d>e:
  print('d>e')
elif d<e:
  print('d<e')
else:
  print('d=e')

x= True
y= False
z = (x and not y) or (y and not x)
print(z)

w = (x!=y)
if w==z:
  print(str(w))
