#Write a Python code that calculates the average of scores that students took in a math class at below.
scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}
output = 0
avg = scores.values()

for i in avg:
   output += i

print(output/8)   