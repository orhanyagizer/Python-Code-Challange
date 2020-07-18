#Please reverse the text below without using text index methods. Please use a loop.
text = input("Please enter a text: ").title().strip()
newtext = ""
for i in range(len(text)-1, -1, -1):
   newtext += text[i]
print(newtext)   


"""text = input("Please enter a text: ").title().strip()

for i in range(len(text)-1,-1,-1):
   print(text[i])"""   

   