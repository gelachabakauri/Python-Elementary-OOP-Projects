#  Basketball points
two_point = int(input("Enter two points quantity : "))
three_point = int(input("Enter three points quantity : "))
two_pts_sum = (two_point * 2)
three_pts_sum = (three_point * 3)
print(" Total Points :  " , two_pts_sum + three_pts_sum)



# Calculator
numb = int(input("Enter first number : "))
action = input( " choose an action : + , - , * , / , % , ^ , ** -----> : ")
numb2 = int(input("Enter second number : "))
if action == "+":
    print(numb + numb2)
elif action == "-":
    print(numb - numb2)
elif action == "*":
    print(numb * numb2)
elif action == "/":
    print(numb / numb2)
elif action == "%":
    print(numb & numb2)
elif action == "^":
    print(numb ^ numb)
elif action == "**":
    print(numb ** numb2)
else:
    print("Are you kidding me?: ")


# Salary Bonus
salary = int(input("Enter your wage : "))
year = int(input("Enter your work year : "))
if year > 5:
    print(salary * 5 / 100)
else:
    print("You will not receive the bonus! ,  Keep your job mate. ")


# students score 
score = int(input("Enter your score : "))
if score >= 91:
    print("You are part of (A) Assessment ")
elif score <= 90 and score >= 81:
    print("you are part of (B) Assessment ")
elif score <= 80 and score >= 71:
    print("you are part of (C) Assessment ")
elif score <= 70 and score >= 61:
    print("you are part of (D) Assessment ")
elif score <= 60 and score >= 51:
    print("you are part of (E) Assessment ")
elif score <= 50:
    print("you are Failure human!")

