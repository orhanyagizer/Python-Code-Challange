#Write a Python code to get lengths of a triangle from a user and then check them
#whether this triangle is equilateral, isosceles or scalene.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


if a == b and a == c:
   print(f"{a}-{b}-{c} is an equilateral triangle.")

elif a != b and a != c and b!=c:
   print(f"{a}-{b}-{c} is a scalene triangle.")
   
elif a == b and a !=c or b ==c and b != a or a == c and a != b :
   print(f"{a}-{b}-{c} is an isosceles triangle.")        
   