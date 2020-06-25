# Python program to display multiplication table of num.Take num value from the user.

num = int(input("Enter the number to display multiplication table: "))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)