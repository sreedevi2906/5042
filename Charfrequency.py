2.Write a Python program to count the number of characters (character frequency) in a string.

In [11]:
string=input('enter a string')
frequency={}
for i in string:
  if i in frequency:
    frequency[i]+=1
  else:
    frequency[i]=1
print(" character frequency of",string,"is",frequency)