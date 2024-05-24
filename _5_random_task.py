#052
import random
number = random.randint(1, 100)
print(number)


#053
import random
fruit = ['Apple' , 'Strawbarry', 'Orange', 'Banana', 'pineApple']
random_fruit = random.choice(fruit)
print(random_fruit)


#054
import random
heads_or_tale = ['h', 't']
random_h_or_t = random.choice(heads_or_tale)
print(random_h_or_t)
choose = input("Choose Heads or Tale: ")
if random_h_or_t == 'h' and choose =='h':
    print("You win")
elif random_h_or_t == 't' and choose =='t':
    print("You winn")
else:
    print("Bad Luck")
print("computer choose: " , random_h_or_t)


#055
import random
random_number = random.randint(1, 5)
print(random_number)
user = int(input("choose a number: "))
if user == random_number:
    print('well done')
while user < random_number:
    print('high')
    user2 = int(input("choose a second number: "))
    if user2 == random_number:
        print("Correct")
        break
    elif user2 != random_number:
        print("you lose")
        break
  
while user > random_number:
    print('low')
    user2 = int(input("choose a second number: "))
    if user2 == random_number:
        print('Correct')
        break
    elif user2 != random_number:
        print("you lose")
        break
      



#056
import random
rand_numb = random.randint(2, 9)
print(rand_numb)
user_numb = int(input("choose a number beetwen 1 and 10: "))
while user_numb != rand_numb:
    user_numb = int(input("choose a number beetwen 1 and 10: "))
print("Finished , you are guess.")



#057
import random
rand_numb = random.randint(2, 9)
print(rand_numb)
user_numb = int(input("choose a number beetwen 1 and 10: "))
while user_numb != rand_numb:
    if user_numb < rand_numb:
        print('high')
    elif user_numb > rand_numb:
        print('low')
    user_numb = int(input("choose a number beetwen 1 and 10: "))
print("Finished , you are guess.")




#058
import random 
quiz = [['10 + 5 ='] , ['20 + 20 ='], ['50 + 50 ='], ['100 - 99 ='], ['500 + 300 =']]
random_quiz = random.choices(quiz)
sum = 0
print(quiz[0])
answer1 = int(input("enter answer: "))
if answer1 == 15:
    sum = sum + 1
    print('correct')
print(quiz[1])
answer2 = int(input("enter answer: "))
if answer2 == 40:
    sum = sum + 1
    print('correct')
print(quiz[2])
answer3 = int(input("enter answer: "))
if answer3 == 100:
    sum = sum + 1
    print("correct")
print(quiz[3])
answer4 = int(input("enter answer: "))
if answer4 == 1:
    print("correct")
    sum = sum + 1
print(quiz[4])
answer5 = int(input("enter answer: "))
if answer5 == 800:
    sum = sum + 1
    print('correct')
print('your total score is: ', sum * 10)
print('you have', sum,'correct out of 5')





#059
import random
color = [['red'], ['blue'], ['green'], ['yellow'], ['purple']]
random_color = random.choice(color)
print(random_color)
user = input("choose a color: ")
if user in random_color:
    print("well done")
else:
    print("i bet you are ", random_color, "with envy" )
while user not in random_color:
     user_try = input("guess again: ")
     print("i bet you are ", random_color, "with envy")
     if user_try in random_color:
        print("Correct")
        break






   
