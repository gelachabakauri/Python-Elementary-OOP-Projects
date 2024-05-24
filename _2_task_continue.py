#012 
first_numb = int(input("Enter first numer : "))
sec_numb = int(input("enter second number : "))
if first_numb > sec_numb :
    print(sec_numb,"\n" ,first_numb)
else:
    print(first_numb , "\n", sec_numb)


#013 
numb = int(input("Enter a number under 20: "))
if numb >= 20:
    print("Too High!")
else:
    print("Thank You.")


#014 
numb = int(input("Enter number between 10 and 20: "))
if numb <10 or numb >20:
    print("Incorrect Answer")
else:
    print("Thank you.")
    

#015
colour = input("Enter your favorite colour: ")
if colour == "red":
    print("I like red too.")
elif colour == "Red":
    print("I like red too.")
elif colour == "RED":
    print("I like red too.")
else:
    print("i don't like this colour, i prefer red.")


#016 
case_up_low = input("It matters to you what case you type ? : ")
if case_up_low == "yes":
    second_ques = input("if it is windy? : ")
    if second_ques == "yes":
        print("it is too windy for an umbrella")
    else:
        print("take an umbrella")
elif case_up_low == "no":
    print("Enjoy your day.")


#017 
age = int(input("how old are you? : "))
if age >= 18 :
    print("You can vote")
elif age == 17:
    print("you can learn")



#018
numb = int(input("enter a number: "))
if numb <=9:
    print("too low")
elif numb >=10 and numb <=20:
    print("Correct")
else:
    print("Too High")

    
    
