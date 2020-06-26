3.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

In [13]:
str1=input("enter a first string")
str2=input("enter a second string")
str1_swap=str2[:1]+str1[1:]
str2_swap=str1[:1]+str2[1:]
print(str1_swap)
print(str2_swap)