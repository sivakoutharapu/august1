#Conditonal statements(if,elif,else)
name = input("enter the name:")

if (name=='siva'):
    print(name)
elif (name=='rama'):
    print(name)
else:
    print("name not match")
    
print()
print()

#Logical operators(and/or/not)
name1 = input("enter the name1:")
name2 = input("enter the name2:")

print(name2=='rama' or name1=='siva')
print(len(name1)>=4 and len(name2)>=4)
print(not (name1!=name2))
    