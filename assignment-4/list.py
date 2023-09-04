# 1. write a python program to merge two lists.
# l1 = eval(input('enter the list1:'))
# l2 = eval(input('enter the list2:'))
# l1.extend(l2)
# print(l1)


# 2. write a python program to find the sum of list elements.
# list_sum = eval(input('enter the list:'))
# print(sum(list_sum))


# 3. write a python program to print even and odd numbers seperatly in list.
# list_num = eval(input('enter the num_list:'))
# list_even = []
# list_odd = []
# for num in list_num:
#     if num%2==0:
#         list_even.append(num)
#     else:
#         list_odd.append(num)    
# print(f'even: {list_even}')
# print(f'odd: {list_odd}')        


# 4. write a python program to delete element of given index in list.
# given_list = eval(input('enter the list:'))
# given_index = int(input('enter the index:'))
# given_list.pop(given_index)
# print(given_list)


# 5. write a python program to delete given elemet from the list 
# given_list = eval(input('enter the list:'))
# given_element = eval(input('enter the value:'))
# given_list.remove(given_element)
# print(given_list)


# 6. write a python program to insert an elemet at given index location.
# given_list = eval(input('enter the list:'))
# given_element = eval(input('enter the value:'))
# given_index = int(input('enter the index:'))
# given_list.insert(given_index,given_element)
# print(given_list)


# 7. write a python program to check the sizes of given two lists are same.
# given_list1 = eval(input('enter the list1:'))
# given_list2 = eval(input('enter the list2:'))
# if len(given_list1)==len(given_list2):
#     print('Sizes of given two lists are same')
# else:
#     print('Sizes of given two lists are not same')    


# 8. Write a Python function that takes two lists and returns True if they have at least one common member.
# given_list1 = eval(input('enter the list1:'))
# given_list2 = eval(input('enter the list2:'))
# count=0
# for i in given_list1:
#     for j in given_list2:
#         if i==j:
#             count+=1
# if count > 0:
#     print(True)
# else:
#     print(False)                
            

# 9. Write a Python program to remove a specified column from a given nested list.
# nested_list = eval(input('enter the list:'))
# print(f'Original Nested list: {nested_list}')
# new_nested_list = []
# for i in nested_list:
#     new_nested_list.append(i[1:])
# print(f'After removing 1st column: {new_nested_list}')    


# 10. Write a Python program to convert a list of multiple integers into a single integer.
# given_list = eval(input('enter the list:'))
# for i in given_list:
#     print(i,end='')


# 11. Write a Python program to remove duplicates from a list.
# given_list = eval(input('enter the list:'))
# new_list = []
# for i in given_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)        



