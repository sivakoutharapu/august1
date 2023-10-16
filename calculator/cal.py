# b = input('choose one add/sub/mult/div: ')

# num1 = int(input('enetr the value: '))
# num2 = int(input('enetr the value: '))

# if b == 'add':
#     print(num1+num2)
# elif b == 'sub':
#     print(num1-num2)
# elif b == 'mult':
#     print(num1*num2)
# elif b == 'div':
#     print(num1/num2)


class Calculator:
    def __init__(self):
        self.reslut = 0
        self.choose_one()
        
    def choose_one(self):
        while True:
            print('1. addition')
            print('2. substraction')
            print('3. multyply')
            print('4. devide')
            print('5. percentage')
            print('6. Reset button')
            print('7. Exit')
            choose_opt = input('choose (1/2/3/4/5/6/7): ')
            if '1' == choose_opt:
                self.addition()
            elif '2' == choose_opt:
                self.substraction()
            elif '3' == choose_opt:
                self.multiply()
            elif '4' == choose_opt:
                self.devide()
            elif '5' == choose_opt:
                self.percentage()  
            elif '6' == choose_opt:
                self.reslut = 0
            else:
                print('Exit program!!!')
                break
    
    def addition(self):
        if self.reslut == 0:
            input_one = int(input('Enter the add_num1: '))
            input_two = int(input('Enter the add_num2: '))
            self.reslut = input_one + input_two
            print(self.reslut)
        else:
            print(self.reslut)
            input_val = int(input('Enter the add_num: '))
            self.reslut += input_val
            print(self.reslut)
        
    def substraction(self):
        if self.reslut == 0:
            input_one = int(input('Enter the sub_num1: '))
            input_two = int(input('Enter the sub_num2: '))
            self.reslut = input_one - input_two
            print(self.reslut)
        else:
            print(self.reslut)
            input_val = int(input('Enter the sub_num: '))
            self.reslut -= input_val
            print(self.reslut)
    
    def multiply(self):
        if self.reslut == 0:
            input_one = int(input('Enter the mul_num1: '))
            input_two = int(input('Enter the mul_num2: '))
            self.reslut = input_one * input_two
            print(self.reslut)
        else:
            print(self.reslut)
            input_val = int(input('Enter the mul_num: '))
            self.reslut *= input_val
            print(self.reslut)
    
    def devide(self):
        if self.reslut == 0:
            input_one = int(input('Enter the div_num1: '))
            input_two = int(input('Enter the div_num2: '))
            self.reslut = input_one / input_two
            print(self.reslut)
        else:
            print(self.reslut)
            input_val = int(input('Enter the div_num: '))
            self.reslut /= input_val
            print(self.reslut)
    
    def percentage(self):
        if self.reslut == 0:
            input_one = int(input('Enter the per_num1: '))
            input_two = int(input('Enter the per_num2: '))
            self.reslut = (input_one / input_two)*100
            print(self.reslut)
        else:
            print(self.reslut)
            input_val = int(input('Enter the per_num: '))
            self.reslut = (self.reslut / input_val)*100
            print(self.reslut)
    
Calculator()      
                  
            