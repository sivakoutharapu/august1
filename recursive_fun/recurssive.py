# Ex-1
# def sqr_num(x):
#     return x*x
# def sqr_sum_list(lst):
#     sum_even_result = 0
#     for i in lst:
#         if i%2==0:
#             sum_even_result+= sqr_num(i)
#     return sum_even_result        

# list_a = [1,2,5,6,7,8]
# result = sqr_sum_list(list_a)
# print(result)

# Ex-2
# def find_power(q,p):
#     if p==0:
#         return 1
#     else:
#         return q * find_power(q,p-1)

# q = 6
# p = 3
# result = find_power(q,p)
# print(result)

# Ex-3
# def list_even_num(lst):
#     lst_even = []
#     lst_odd = []
#     for i in lst:
#         if i%2==0:
#             lst_even.append(i)
#         else:
#             lst_odd.append(i)    
#     return f'even: {lst_even}',f'odd: {lst_odd}'

# list_a = [1,2,3,4,5,7,89,34,48,55]
# result= list_even_num(list_a)
# print(result)
