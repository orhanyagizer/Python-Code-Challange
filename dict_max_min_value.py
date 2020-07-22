#Write a Python code that finds the students who have maximum and minimum average at a given dictionary below.

scores = {'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, 
 'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, 
 'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, 
 'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, 
 'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}

maxavr, minavr = 0, 100
for i in scores:
   average = sum(scores[i].values())/len(scores[i].values())
   if average > maxavr:
       maxavr = average
       maxkey = i
   if minavr > average:
       minavr = average
       minkey = i
   print(f"{i}   {average:.1f}")
print(f"\n{maxkey} has maximum average with a score {maxavr}\n{minkey} has minimum average with a score {minavr}")