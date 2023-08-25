# 1.Write a python program to remove a given  character from string.

# Ex-1
# string = input('enter the word:')
# letter = input('enter the character:')
# find_index = string.find(letter)
# a = string[:find_index]
# b = string[find_index+1:]
# str_result = a+b
# print(str_result)

# Ex-2
# string = input('enter the word:')
# index = int(input('enter the index:'))
# a = string[:index]
# b = string[index+1:]
# str_result = a+b
# print(str_result)


# 2.Write a program to check String is Palindrome or not

# string = input('enter the palindrome:')
# slice_a = string[::-1]
# if string == slice_a:
#     print("Palindrome")
# else:
#     print("not a palindrome")    


# 3.Write a python program to check given character is vowel or consonant

# string = input('enter the character:')
# str_lower = string.lower()
# if ("a"==str_lower or "e"==str_lower or "i"==str_lower or "o"==str_lower or "u"==str_lower):
#     print("it's a vowel")
# else:
#     print("it's a consonant")    


# 4.Write a python program to replace string space with given character in Python

# string = input('enter the sentence:')
# str_replace = input('enter the replace word:')
# print(string.replace(str_replace," "))


# 5.Write a python program to count alphabets, digits, and special characters in the string

# string = input('enter the value:')
# count = 0
# count1 = 0
# count2 = 0
# for i in string:
#     if i.isalpha():
#         count+=1
#     elif i.isdigit():
#         count1+=1   
#     else:
#         count2+=1
# print(f'Alphabets count        : {count}') 
# print(f'Digits count           : {count1}') 
# print(f'Special character count: {count2}')  


# 6.Write a python program to remove all the blank spaces in a given string

# string = input('enter the value:')
# str_strip = string.strip()
# print(str_strip)            


# 7.Write a python program to find sum of integers in the string

# string = input('enter the numbers:')
# sum_int = 0
# for i in string:
#     sum_int+=int(i)
# print(f"sum of integer: {sum_int}")    


# 8.Write a python program to Remove Repeated Character from String

# string = input("enter the value:")
# str_char = ''
# for char in string:
#     if char not in str_char:
#         str_char+=char
# print(str_char)             


# 9.Write a python program to count occurrence of given character in string

# string = input('enter the value:')
# character = input('enter the character:')
# count_character = string.count(character)
# print(count_character)


# 10.Write a python program to check string is anagrams or not in Python

# string1 = input('enter the value:')
# string2 = input('enter the value:')
# count=0
# for i in string1:
#     for j in string2:
#         if i==j:
#             count+=1
#             break
# if count==len(string1):
#     print('Both strings are anagrams')
# else:
#     print('Both strings are not anagrams')
