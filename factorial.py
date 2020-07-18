#calculate factorial of a number 
number = int(input("Please enter a number: "))
factorial = 1

while number<0:
   print("Please enter a poisitive number or zero: ")
   number = int(input("Please enter a number: "))

if number >0:
   for i in range(number,0,-1):
      factorial *= i
   
elif number ==0:
   factorial =1 
      
print(f"{number}! = {factorial}")     
   