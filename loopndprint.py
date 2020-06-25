# Python program to take 10 integers from keyboard using loop and print their average value on the screen.

sum = 0

i = 10
while i>0:
  print ("Enter number")
  num = int(input())
  sum = sum + num
  i = i-1
print ("average is",sum/10.0)
# to print the patern
i = 1
while i<=4:
  print ("*"*i)
  i = i+1