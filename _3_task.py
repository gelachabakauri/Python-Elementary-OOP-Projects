#1 Temperature Converter

celsius = int(input("Enter a temperature in Celsius : "))
fahrenheit = celsius * 9/5 + 32
print(fahrenheit) 


#2 Grade Calculator

math = int(input("Enter your mark of Math: "))
science = int(input("enter your mark of Science: "))
english = int(input("Enter your mark of English: "))
sum = (math + science + english) / 3
print("your avarage is: " ,  sum)

#3 Simple ATM

pin = input("enter your PIN: ")
if pin == "1234":
    print("granted access")
else:
    print("Error!")


#4 Online Shopping
cost = int(input("Enter your whole cost: ")) 
total_cost = cost * 10 / 100
discount_cost = cost - total_cost
if cost >= 600:
    print("you have discount of 10 % , and you need to pay: " , discount_cost)
else:
    print("you don't have discount")



#5 Email Validator


email = input("Enter your mail e.g., contain '@' symbol: ")
if '@' in email:
    print("your mail is verified.")
else:
    print("try again!")


#6 Pizza Topping Selection

pizza = input("choose a Pizza from Menu:\n \npeperoni \nmargarita\npork deluxe\nveggie\n----: ")
if 'peperoni' in pizza:
    print("It will be ready in 15 minutes")
elif 'margarita' in pizza:
    print("It will be ready in 15 minutes")
elif 'pork deluxe' in pizza:
    print("It will be ready in 15 minutes")
elif 'veggie' in pizza:
    print("It will be ready in 15 minutes")
else:
    print("we don't have this pizza!")


#7 Pet Adoption Eligibility


age = int(input("Enter your age: "))
pet_have = input("have you pet? or Have you ever had? ")
if age >= 21 and pet_have == 'yes':
    print("you are eligible to adopt a pet from a local shelter.")
elif age >= 21 and pet_have =='no':
    print("we think you mayebe eligible to adopt a pet from a local shelter.")
else:
    print("you don't have a permission!")



#8 Movie Ticket Pricing

age = int(input("enter your age: "))
movie_type = input("enter the type of movie: ")
child_price = 8
adult_price = 15
if age >= 18 and movie_type == 'adult':
    print("adult price is " , adult_price ,'$')
elif age < 18 and movie_type =='child':
    print("childe price is ", child_price, "$")
else:
    print("your choise is incorrect!")



#9 Fruit Salad Ingredients


fruit = input("enter your favorite Fruit: ")
fruit_salad = "Orange , orange , Bannana , bannana, Apple, apple, Pineapple , pineapple, Strawberry , strawberry"
if fruit in fruit_salad:
    print("this fruit is avialable for salad.")
else:
    print("this fruit not included fruit salad!")


#10 Homework Planner


day = input("Enter current day of the week: ")
if day == 'monday':
    print("you need to complete Math homework.")
elif day == 'tuesday':
    print("you need to complete English homework")
elif day == 'wednesday':
    print("you need to complete science homework")
elif day == 'thursday':
    print("you need to complete math and English homework")
elif day == 'friday':
    print("tommorow is saturday , you can relax.")
else:
    print("you can sleep ")


#11 Weather Clothing Recommendation

temperature = int(input("Enter a current Temperature: "))
hot = "shorts and T-shirts"
cold = "Jacket"
if temperature >= 30:
    print("It is recommended that you wear it" , hot)
else:
    print("It is recommended that you wear it" , cold)


#12 Healthy Food Choice
food = input("Enter your favorite food: ")
healthy = "sandwich , fish , brocoli, peanut, rice, chicken"
unhealthy = "khinkali, shawarma , burger, pork, bacon, sausage, cake"
if food in healthy:
    print("it is healthy food for your life.")
elif food in unhealthy:
    print("it is unhealthy food for you.")
else:
    print("this food is not our menu. order another one.")



#13 Game Score Ranking

score = int(input("Enter your game score: "))
beginner = "you are beginner"
intermediate = "you are on intermediate"
advanced = "you are on advanced level"
if score <= 3:
    print(beginner)
elif score <=6:
    print(intermediate)
else:
    print(advanced)


#14 Sports Team Selection


age = int(input("Enter your age: "))
sports = input("what is your favorite sport? ")
eligible = "you are eligible to join "
if age <= 8 and sports == 'football':
    print(eligible , 'football')
elif age <=15 and sports == 'swimming':
    print(eligible , "swimming")
elif age <=25 and sports == 'basketball':
    print(eligible , "basketball")
else:
    print("you are not eligible for this sport. ")



#15 Music Genre Recommendation


mood = input("enter your mood for choose Music Genre: ")
if mood == 'happy':
    print("i reccomend PoP Genre")
elif mood == 'sad':
    print("i recomend motivation music")
elif mood == 'energetic':
    print("i recomend Electronic music")
elif mood == 'relaxed':
    print("i recomed chill music")
else:
    print("go sleep!")


#16 Discount price Calculator

pound = int(input("Enter a price in pounds: "))
percentage = int(input("Enter percentage: "))
discount =  pound * percentage / 100 
price_after_discount = pound - discount
if pound >= 400 and percentage == 20:
    print("discount is " , discount , "£")
    print("price after discount : " , price_after_discount , "£")   
else:
    print("we have only 20 '%' discount over 399 £ ")



#17 game up and down


guess_number = 44
numb = int(input("enter number: "))
if numb < 44:
    print("UP")
elif numb > 44 :
    print("Lower")
else:
    print("you are guess")


#18 Cake Sale 
cupcake = int(input("how many cupcakes do you plan to sell? "))
macaron = int(input("how many macarons do you plan to sell? "))
cheesecake = int(input("how many cheescake do you plan to sell? "))
cupcake_price = 40 
macaron_price = 50 
cheesecake_price = 70 
income = cupcake * cupcake_price + macaron * macaron_price + cheesecake * cheesecake_price
print("total income: " , income , "P")



#19 Weight on the Moon


weight = int(input("Enter your weight on the Earth:  "))
calculates = (weight / 9.81) * 1.622
print("your Weight on the Moon is: ", calculates)


#20 Stopwatch 

number = 45015
hours = number // 3600
reminder = number % 3600 
minutes = reminder // 60
seconds = reminder % 60
print(f'{number}  seconds =  {hours}  hours  {minutes}  minutes  {seconds}  seconds' ) 


#21 Leap year

year = int(input("input a year: "))
if year % 4 == 0:
    print(year , "is a leap year")
else:
    print(year , "is not a leap year")


#22 Winter Olympic 

winterolympic = 2022
next = winterolympic + 4
print("next olympic will be in " , next)



#23 multiple table *

number = input("enter number: ")
for i in range(10):
    product = number * i
    print(f'{number} + "x" + i + "=" + {product}')



#24 Login form

username = input("enter username: ")
password = input("enter password: ")
if username == 'admin' and password == '1234':
    print("you are logged in.")
else:
    print("incorrect username or password")


#python for loop ##################


#1 
name = input("enter your name:")
for i in range(4):
    print(name)


#2 
name = input("enter your name: ")dd
numb = int(input("enter number: "))
for i in range(numb):
    print(name)


#3
name = input("enter your name: ")
for x in name:
    print(x)

#4 
numb = int(input("enter number less than 50: "))
for i in range(numb):
    print(numb)
    numb = numb -1 


#5 
name = input("Enter your name: ")
numb = int(input("Enter number: "))
if numb > 10:
    for i in range(3):
        print("it's very high")
else:
    for i in range(numb):
        print(name)


#6 
for i in range(2, 20, 2):
    print(i)


#7
for i in range(20, 2, -2):
    print(i)



#8
word = input("Enter a word 'information': ")
print(word.replace("i", ""))


#9
x = "#"
for i in range(7):
    print(x)
    x = x + "#"


#10
x = "########"
for i in range(8):
    print(x)
    

#11
sum = 0
for i in range(1, 101, 2):
   print(i)
   sum = sum + i
print(sum)
    

#12
sum = 0
for i in range(0, 101, 2):
    print(i)
    sum = sum + i 
print(sum)


#13
sum = 0
numb = int(input("Enter number: "))
numb2 = int(input("Enter number: "))
for i in range(numb, numb2):
    print(i)
    sum = sum + i
print(sum)


#14
word = "anaconda"
for i in word:
    print(i)


#15
num = int(input("Enter number: "))
for i in range(1, num, 2):
    print(i)
for i in range(2 , num, 2):
    print(i)
    i = i + 2
    

#16 
first = "fizz"
second = "buzz"
third = "fizzbuzz"
numb =  int(input("enter a number: "))
if numb % 15 == 0:
    print(third)
elif numb % 5 == 0:
    print(second)
elif numb % 3 == 0:
    print(first)
else:
    print("This number don't divede to non of them")


#17
sitkva = "python"
print(sitkva[::-1])


#18
sitkva = "Hello"
if "H" in sitkva or "e" in sitkva or "o" in sitkva or "u" in sitkva or "h" in sitkva or "a" in sitkva:
    print("სიტყვა შეიცავს ხმოვნებს")
else:
    print("სიტყვა მხოლოდ თანხმოვნებს შეიცავს.")


#19
number = 12345
for i in range(1, 6, 1):
    number = i * i
    print(number)
    

#20
character = "‡"
for i in range(1, 6, 1):
    print(character)
    character += "‡"

    
        



