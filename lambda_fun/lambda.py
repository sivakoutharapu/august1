# Ex-1
# print('Adding by using lambda: ')
# n = 9
# result = lambda a: a * n
# for i in range(1,11):
#     print(result(i))


# Ex-2
# print('finding sum of value even or odd:')
# a = 2
# b = 4
# c = 8
# result = lambda a,b,c : 'even' if (a+b+c)%2==0 else 'odd'
# print(result(a,b,c))


# Ex-3
# print('using comprehension method in lambda multiplying:')
# num_value = [lambda arg=x : arg * 10 for x in range(12,20)]
# for num in num_value:
#     print(num())


# Ex-4
# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# # Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)
# # Get the second largest element
# secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
# res = secondLargest(List, sortList)
# print(res)
