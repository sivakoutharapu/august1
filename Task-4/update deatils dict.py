
employ_details = {
    101: {'Name': 'siva', 'EmpID': 101, 'Domain': 'python', 'Email': 'sivaram@gmail.com'}, 
    102: {'Name': 'rama', 'EmpID': 102, 'Domain': '.net', 'Email': 'rama123@gmail.com'},
    103: {'Name': 'krishna', 'EmpID': 103, 'Domain': 'java', 'Email': 'krishna1223@gmail.com'},
    }

# employ_details = {}

def add_employ_details():
    name = eval(input("Enter the name    : "))
    empid = eval(input("Enter the empid  : "))
    domain = eval(input("Enter the domain: "))
    email = eval(input("Enter the email  : "))
    
    employee = {
        'Name'  :name,
        'EmpID' :empid,
        'Domain':domain,
        'Email' :email,
    }
    
    employ_details[empid] = employee
    
# for i in range(3):
#     add_employ_details()    

print(employ_details)

check_add_remove_update = input('Enter check or add or remove or update details: ')

if check_add_remove_update == 'check':
    given_empid = eval(input('Check empid: '))
    if given_empid in employ_details:
        print(employ_details[given_empid])
    else:
        print('Employee details not found')
elif check_add_remove_update == 'add':
    add_employ_details()
    print(len(employ_details))
elif check_add_remove_update == 'remove':
    given_empid = eval(input('Remove empid: '))
    if given_empid in employ_details:
        del employ_details[given_empid]
        print(employ_details)
    else:
        print('Employee details not found')
elif check_add_remove_update == 'update':
    given_empid = eval(input('Update empid: '))
    
    if given_empid in employ_details:
        key_name = eval(input('Enter key name: '))
        update_value = eval(input('Enter the Update value: '))
        employ_details[given_empid][key_name] = update_value
        print(employ_details[given_empid])
            
else:
    print('Enter correct value')
