#Creating table using while loop and For loop
print("Using while loop create tabel")
number1 = int(input("while loop num:"))
count = 1
while count<=10:
    print(number1," x ",count, " = ",count*number1)
    count+=1
print("------------------------------------------")

print("Using for loop create table")
number2 = int(input("for loop num:"))
for num in range(1,11):
    print(number2," x ",num," = ",num*number2)
    
