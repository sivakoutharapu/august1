# 1.Write a Python script to add a key to a dictionary.
# dict_a = {0: 10, 1: 20}
# print(f'without add key: {dict_a}')
# dict_a[2]=20
# print(f'add a key: {dict_a}')


# 2.Write a Python script to check whether a given key already exists in a dictionary.
#Sample: {'name':'sivaram','gender':'male','age':28,'emp_id':'MT-01838'}
# dict_a = eval(input('enter the dict: '))
# key_a = eval(input('enter the dict: '))
# key_value = ''
# for key in dict_a.keys():
#     if key == key_a:
#         key_value=f'Key is present and value of the key is:{dict_a[key]}'
#         break
#     else:
#         key_value='Key isn\'t present!'
# print(key_value)        


# 3.Write a Python program to iterate over dictionaries using for loops
# dict_a = eval(input('enter the dict: '))
# for item in dict_a.items():
#     print(item)


# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# dict_a = {}
# for item in range(1,16):
#     dict_a[item] = item**2
# print(f'Square of the keys: {dict_a}') 

   
# 5.Write a Python program to create a dictionary from a string.
# str_a = eval(input('enter the dict: '))
# dict_a={}
# for letter in str_a:
#      dict_a[letter] = str_a.count(letter)
# print(str_a)
# print(dict_a)     


# 6. Write a Python program to sum all the items in a dictionary.
# dict_a = eval(input('enter the dict: '))
# sum1 = 0
# for value in dict_a.values():
#     sum1+=value
# print(f'Sum of values: {sum1}')    
    

# 7.Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}  d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# dict_a = eval(input('enter the dict: '))
# dict_b = eval(input('enter the dict: '))
# new_dict = dict_b
# for key,value in dict_a.items():
#     if key in dict_b:
#         new_dict[key] = value + dict_b[key]
#     else:
#         new_dict[key] = value
# print(new_dict)            

# 8.Write a Python program to access dictionary key's element by index.
# dict_a = eval(input('enter the dict: '))
# for i in range(len(dict_a)):
#     print(list(dict_a)[i])
# Expected Output:
# physics
# math
# chemistry


# 9.Write a Python program to remove a key from a dictionary.
# dict_a = eval(input('enter the dict: '))
# str_a = eval(input('enter the del key:'))
# print(dict_a)
# del dict_a[str_a]
# print(dict_a)


# 10.Write a Python script to merge two Python dictionaries.
# dict_a = eval(input('enter the dict1: '))
# dict_b = eval(input('enter the dict2: '))
# print({**dict_a,**dict_b})

# dict_a.update(dict_b)
# print(dict_a)





