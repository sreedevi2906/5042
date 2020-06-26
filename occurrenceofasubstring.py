6.Write a Python program to count occurrences of a substring in a string.

In [36]:
string=input('enter a string')
substring=input('enter a substring')
frequency=len(string.split(substring))
print("number of times substring is",substring,"has repeated in",string,"is:",frequency)