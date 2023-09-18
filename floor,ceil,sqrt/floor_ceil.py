import math

# floor() method in Python returns the floor of x i.e., 
# the largest integer not greater than x. 
print ("math.floor(-23.11) : ", math.floor(-23.11))   # ouput: -24
print ("math.floor(300.16) : ", math.floor(300.16))   # ouput: 300
print ("math.floor(300.72) : ", math.floor(300.72))   # ouput: 300



# The method ceil(x) in Python returns a ceiling value of x i.e., 
# the smallest integer greater than or equal to x.
print ("math.ceil(-23.11) : ", math.ceil(-23.11))   # ouput: -23
print ("math.ceil(300.16) : ", math.ceil(300.16))   # ouput: 301
print ("math.ceil(300.72) : ", math.ceil(300.72))   # ouput: 301



# The math.sqrt() method returns the square root of a number.
# Note: The number must be greater than or equal to 0.
# If the number is less than 0, it returns a "ValueError". 
# If the value is not a number, it returns a "TypeError"

print(math.sqrt(9))   # output: 3
print(math.sqrt(6.6)) # output: 2.569046515733026
print(math.sqrt(3))   # output: 1.7320508075688772
# print(math.sqrt(-2))   # output: value error
# print(math.sqrt('g'))  # output: type error


