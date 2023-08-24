#1 Membership operator(in,not in)
print('Membership(in,not in):')
#Ex-1
tuple_string = "1","2","3","4","5"
string1 = "6" in tuple_string
print(string1)
#Ex-2
word_string = "python is a easy language"
string1 = "is" in word_string
print(string1)
#Ex-3
word_string = "python is a easy language"
string1 = "easy" not in word_string
print(string1)
print()


#2 Remove spaces from given string(strip())
print("strip():")
#Ex-1
number_str = "  1234567890   "
num_str = number_str.strip()
print(number_str)
print(num_str)
#Ex-2
name_str = " ...k.siva rama krishna... "
num_str = name_str.strip(' .')
print(name_str)
print(num_str)
#Ex-3
name_str = "...//k.siva rama krishna//..."
num_str = name_str.strip('./')
print(name_str)
print(num_str)
print()


#3 Comparing two strings
print('Comparing strings:')
#Ex-1
name1 = 'siva'
name2 = 'Siva'
print(name1==name2)
#Ex-2
name1 = 'python'
name2 = 'Java'
print(name1>name2)
#Ex-3
name1 = 'rama'
name2 = 'ravi'
print(name1<=name2)
print()


#4 Find substring by using index method(index())-first occurence
print("index():")
#Ex-1
string = "Python is an easy to learn"
string1 = string.index('n')
print(string1)
#Ex-2
string = "Rakshabandhan"
string1 = string.index('a')
print(string1)
#Ex-3
string = "Python is an easy to learn"
string1 = string.index(' ',7,15)
print(string1)
print()


#5 Find substring by using rindex method(rindex())-least occurence
print('rindex():')
#Ex-1
string = "Python is an easy to learn"
string1 = string.rindex('n')
print(string1)
#Ex-2
string = "Rakshabandhan"
string1 = string.rindex('a')
print(string1)
#Ex-3
string = "Python is an easy to learn"
string1 = string.rindex(' ',7,15)
print(string1)
print()

#6 Find substring by using find method(find())-first occurence
print("find():")
#Ex-1
string = "Python is an easy to learn"
string1 = string.find('m')
print(string1)
#Ex-2
string = "Rakshabandhan"
string1 = string.find('a')
print(string1)
#Ex-3
string = "Python is an easy to learn"
string1 = string.find(' ',7,15)
print(string1)
print()

#7 Find substring by using rfind method(rfind())-least occurence
print("rfind():")
#Ex-1
string = "Python is an easy to learn"
string1 = string.rfind('n')
print(string1)
#Ex-2
string = "Rakshabandhan"
string1 = string.rfind('a')
print(string1)
#Ex-3
string = "Python is an easy to learn"
string1 = string.rfind(' ',0,6)
print(string1)
print()

#8 separating string by using split method
print("split():")
#Ex-1
num_str = '22-08-1996'
str_split = num_str.split('-')
print(str_split)
#Ex-2
num_str = 'rakhi festival is coming'
str_split = num_str.split()
print(str_split)
#Ex-3
num_str = 'M a r o l i x'
str_split = num_str.split()
print(str_split)
print()
#9 Replace the word by using replace method
print('replace():')
#EX-1
string = 'python is a hard language'
str_rep = string.replace('hard','sensitive')
print(string)
print(str_rep)
print()
#Ex-2
string = 'hello, i am bad in python'
str_rep = string.replace('bad','good')
print(string)
print(str_rep)
print()
#Ex-3
string = 'rakhi festival next month august'
str_rep = string.replace('next','this')
print(string)
print(str_rep)
print()
#10 Join the string by using join method
print("join():")
#Ex-1
date = '22','08','1996'
date_join = '/'.join(date)
print(date_join)
#Ex-2
name = 'siva','rama','krishna'
name_join = ' '.join(name)
print(name_join)
#Ex-1
company = 'MAROLIX'
company_join = '-'.join(company)
print(company_join)