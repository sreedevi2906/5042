 X=float(input('enter the radius of the circle'))
Y=int(input('enter the value of central angle in degrees:'))
import math
part_one= (math.pow(X,2))/2
part_two= ((((math.pi)/180)*Y)-math.sin(Y))
area= part_one*part_two
print("Area of the segment of a circle of radius",X, "and central angle",Y,"is:",area)