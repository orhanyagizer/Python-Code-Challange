#Print the prime numbers which are between 1 to entered limit number (n).

num = int(input("Please enter a number: "))
emp_list = []


for i in range(2,num+1):
   bolundu = False
   for j in range(2,i):
      if i % j == 0:
         bolundu = True
         
   if bolundu == False:
      emp_list.append(i)        
   

print(emp_list) 


