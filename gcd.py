# Python program to find greatest common divisor (gcd) or highest common factor of given two numbers.

def gcd(a,b): 
       
    if (a == 0): 
        return b 
    if (b == 0): 
        return a 
   
    if (a == b): 
        return a 
  
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a) 
   
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if(gcd(a, b)): 
    print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
    print('not found')