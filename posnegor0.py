2.python program to check if a number is positive,negative or 0

In [12]:
num=int(input('enter a number'))
if(num==0):
  print("num is zero")
else:
  if num>0:
   print("num is positive")
  else:
   print("num is negative")