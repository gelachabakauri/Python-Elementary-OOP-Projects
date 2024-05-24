#  001 
name = input(str("What is your Name? :  "))
print(' Hello , ' , name , '!')


# 002 
name = input(str("What is your Name? : "))
surname = input(str("What is your Surname? : "))
print("Hello ," , name , surname , "! ")


# 003
print("Why do you call a Bear with no teeth ?")
print("A Gummy Bear! ")

# 004
number = int(input("Enter a First Number : "))
number2 = int(input("Enter Second Number : "))
total_sum = (number + number2)
print( "the total is : " , total_sum)


# 005
numb = int(input("Enter first number : "))
numb2 = int(input("enter second number : "))
numb3 = int(input("enter a third number : "))
total_sum2 = (numb + numb2) * numb3
print( "the answer is : " , total_sum2)



# 006
ask = int(input("how many slices of pizza the user started with ? "))
ask2 = int(input("how many slices they have eaten ? "))
total_sum3 = (ask - ask2)
print("They have left : " , total_sum3 , "slices of Pizza " )


# 007
name = input(str("What is your Name? : "))
age = int(input("How old are you? : "))
get_age = (age + 1)
print("Next birthday you will be : " , get_age )

# 008 
ask3 = int(input("what total price of the bill? : "))
print(ask3 , "$")
ask4 = int(input("how many dinners are there? : "))
print( "there are" , ask4 , "dinner " )
pay =  ( ask3 / ask4 )
print("each person must pay : " , pay , "$")


# 009
days = int(input("how many days are : "))
hour = ( days * 24)
minute = ( days * 24 * 60)
second = ( days * 24 * 60 * 60)
print("hours :" , hour,       "  minutes :", minute, " seconds : " , second)



# 010
weight = int(input("enter a weight in killograms : "))
pound = float(2.204)
print(weight * pound , "pounds")


# 011
numb1 = int(input("Enter a number over 100:---->  "))
numb2 = int(input("Enter a number over 10---->: "))
answer = (numb1 / numb2)
print( "smaller number goes into the larger number " ,answer, "times ")