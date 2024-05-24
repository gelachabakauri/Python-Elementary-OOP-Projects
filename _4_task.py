#1 BMI Task

def bmi( height = float(input("enter your height: ")), weight = int(input("Enter your weight: "))):
    print("your BMI is " ,  weight / height **2)
bmi()



#2 Rectangle Area
def rectangle(length = int(input("Enter rectangle length: ")) , width = int(input("Enter rectangle width: "))):
    print("Area = ", length * width)
    print("Perimeter = " , 2*(length + width ))

rectangle()


#3 Calculator
def calc(numb = int(input("Enter a number: ")) , action = input("choose an action: -, +, / , *  "), numb2 = int(input("enter second number: "))):
    if action == "-":
        print('sum =',numb - numb2)
    elif action == "+":
        print('sum =',numb + numb2)
    elif action == '/':
        print('sum =',numb / numb2)
    elif action == "*":
        print('sum =',numb * numb2)
    else:
        print("please enter right format")

calc()


#4 Odd or Even, Positive or Negative


def oddoreven(numb = int(input("Enter a number: "))):
    if numb % 2 != 0:
        print("it is Odd")
    else:
        print("it is Even")

oddoreven()


def posneg(numb = int(input("Enter number: "))):
    if numb >= 0:
        print("Positive", numb)
    else:
        print('Negative' , numb)

posneg()


#5 CocaCola Case 

def cola():
    cent = int(input("Enter 5 , 10 or 25 cent , CocaCola's price is 50 cent :"))
    money = 50 - cent
    left = money
    while cent < 50:
        print("you left : ", left , "Cent for CocaCola" )
        cent = int(input("Enter 5 , 10 or 25 cent , CocaCola's price is 50 cent :"))
        left = left - cent
        if left == 0:
            print("your Cola is prepearing.")
            break
        #print("your left : ", left )
        
        
    
cola()


#6 Teacher Salary 

def salary_wage():
    salary = 30000
    for i in range(1, 11):
        salary = salary + (salary * 0.02)
        print(salary)

salary_wage()





 