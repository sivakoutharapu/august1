from functools import reduce
import operator
import itertools

# # Ex-1
# list_a = [1, 2, 3, 4, 5]
# print("The sum of the list elements is : ", end="")
# result = reduce(lambda a,b: a+b,list_a)
# print(result)
# print("The sum of the list elements is : ", end="")
# result1 = reduce(operator.add,list_a)
# print(result1)

# print("The summation of list using accumulate is :", end="")
# result2 = itertools.accumulate(list_a,lambda a,b: a+b)
# print(list(result2))

# print("The product of the list elements is : ", end="")
# result3 = reduce(operator.mul,list_a)
# print(result3)

# print("The concated product is : ", end="")
# result4 = reduce(operator.add,['siva',' rama',' krishna'])
# print(result4)


# # Ex-2
# words_lst = ['search','longest','word','keyword']
# result = reduce(lambda a,b: a if a>b else b,words_lst)
# print(result)


# Ex-3
# list_a = [11, 232, 343, 34347, 34328, 1, 55, 6, 77]
# result = reduce(lambda a,b: a if a%3==0 else b,list_a)
# print(result)
