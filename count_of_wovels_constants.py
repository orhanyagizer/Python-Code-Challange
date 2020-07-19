#Write a Python code that counts how many vowels and constants a string has that a user entered.

vowel_list = []
constant_list = []
word = input("Please enter a word: ").lower()


for i in word:
   if i in set("aeiou"):
      vowel_list.append(i)
      count_vowel = len(vowel_list)
   else:
      constant_list.append(i)
      count_constant = len(constant_list)
         
      
print(f"'{word}'\nVowels: {vowel_list}. The number of vowels is {count_vowel}.\nConstants: {constant_list}. The number of constants is {count_constant}.")      
      