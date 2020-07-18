"""Write a Python code to sort the list at below without using .sort() method of list.
elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
Expected output:
[2, 11, 12, 45, 77, 99, 333, 999, 8982]"""

my_list = [999,333,2,8982,12,45,77,99,11]


for i in range(len(my_list)):  # 0-8
   for j in range(i+1,len(my_list)):  # 1-8
      if my_list[i]> my_list[j]:
         temp = my_list[i]
         my_list[i] = my_list[j]
         my_list[j] = temp

print(my_list)          
         