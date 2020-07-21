#Define a “function” to calculate permutation of 2 numbers.
#Reminder: P(n,r) = n!/(n-r)!
#Clue: Defining a function that calculates factorial of given number, may be helpful.


def permutation(a,b):
   per = 1
   per1 = 1
   diff = a-b
   for i in range(a,0,-1):
      per *= i
      
   for i in range(diff,0,-1):
      per1 *= i
      
      
   return int(per/per1)   
      

print(permutation(5,2))
print(permutation(6,3))