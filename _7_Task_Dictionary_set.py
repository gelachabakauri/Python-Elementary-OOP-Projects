#1
thisdict = {
    0: 10,
    1: 20,
    2: 30
}
print(thisdict)



# 2
thisdict = {
    'striker': 'darwin',
    'winger': 'salah',
    'cb': 'vvd'
}

if 'striker' in thisdict.keys():
    print("Yes")


#3
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

#4
def Merge(first_dict, second_dict):
    return(second_dict.update(first_dict))

first_dict: dict = {'Allison': 1, 'Joe Gomez': 2, 'Wataru endo': 3, 'VVD': 4}
second_dict: dict = {'Konate': 5, 'Thiago': 6, 'Diaz': 7, 'Szoboslai': 8}

print(Merge(first_dict, second_dict))
print(second_dict)



#5 
thisdict = {
    'brand': 'Alienware',
    'cpu': 'intel',
    'gpu': 'nvidia'
}
del thisdict['cpu']
print(thisdict)



#6
d_ct = {
    'two': 2,
    'three': 3,
    'four': 4
}

sum = 1

for i in d_ct:
    sum = sum * d_ct[i]
print(sum)


#7
some_dict: dict = {'Allison': 1, 'Trent': 66, 'Robertson': 26, 'Jota': 20}
sum = 0
for i in some_dict.values():
    sum = i + sum
print(sum)


#8
dct = {
    'a': 10,
    'b': 50,
    'c': 100
}

print("max value is : ", max(dct.values()))
print("min value is : ", min(dct.values()))



#9
nested_dict: dict = {'dct1': {'Name': 'Bobby', 'Team': 'Liverpool fc', 'Nationality': 'Brazil'} ,
                     'dct2': {'Name': 'Bobby', 'Team': 'Liverpool fc', 'Nationality': 'Brazil'},
                     'dct3': {'Name': 'Fabinho', 'Team': 'Liverpool fc', 'Nationality': 'Brazil'}}

if nested_dict['dct1'] == nested_dict['dct2']:
    print('yes')
    del nested_dict['dct2']
elif nested_dict['dct1'] == nested_dict ['dct3']:
    print('same both')
    del nested_dict['dct3']
elif nested_dict['dct2'] == nested_dict['dct3']:
    print("both same")
    del nested_dict['dct3']
print(nested_dict)


#10
just_dict: dict = {'coach': 'Klopp', 'Director': 'Edwards', 'Legend': 'Dalglish'}
if len(just_dict) == 0:
    print("the dict is empty ")
else:
    print("the dict is not empty")


#coplex task #2
start_numb = 0
second_num = 1
fibonachi = 0
while fibonachi < 89:
    fibonachi = start_numb + second_num
    print(fibonachi)
    start_numb = second_num
    second_num = fibonachi




#3 password generator
import random
special_char: list = ['!', '@','#','$','%','^','&','*','(',')','-', '_','+', '=']
alphabet: list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o', 'p','q','r','s','t','u','v','w','x','y','z']
numb: list = ['1','2','3','4','5','6','7','8','9','0']
choose_1: str = input("choose your password length min 8 and max 12  : ")
choose_2: str = input("do you want include your passwor with 'Uppercase ? ")
rand_char = random.choice(special_char)
rand_alph = random.choice(alphabet)
rand_num = random.choice(numb)
all = rand_char + rand_alph + rand_num
all_2 = random.choice(special_char)
all_alph2 = random.choice(alphabet)
all_num = random.choice(numb)
char_3 = random.choice(special_char)
alph_3  = random.choice(alphabet)
all3 = all + all_2
all_in = all3 + all_num + all_2 + char_3 + alph_3
if choose_2 == 'yes' and choose_1 == '8':
    print(all_in.upper())  
elif choose_2 == 'no' and choose_1 == '8':
    print(all_in)
elif choose_2 == 'yes' and choose_1 == '9':
    print(all_in.upper() + rand_char)
elif choose_2 == 'no' and choose_1 == '9':
    print(all_in + rand_char)
elif choose_2 == 'yes' and choose_1 == '10':
    print(all_in.upper() + rand_char + rand_num)
elif choose_2 == 'no' and choose_1 == '10':
    print(all_in + rand_char + rand_num)
elif choose_2 == 'yes' and choose_1 == '11':
    print(all_in.upper() + rand_char + rand_num + rand_char)
elif choose_2 == 'no' and choose_1 == '11':
    print(all_in + rand_char + rand_num + rand_char)
elif choose_2 == 'yes' and choose_1 == '12':
    print(all_in.upper() + rand_char + rand_num + rand_char + rand_num)
elif choose_2 == 'no' and choose_1 == '12':
    print(all_in + rand_char + rand_num + rand_char + rand_num)
print("your password generated!")




#4 

numb: list = [1,2,3,4,5,6,7,8,9,10]
check = int(input("check if this number is here ? "))

if check in numb:
    print(True)
else:
    print(False)



#5

numb = list(input("Enter 3 Number with space between them: ").split())

a = int(numb[0])
b = int(numb[1])
c = int(numb[2])

if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c


print("the largest number is: " , largest)