#105
f = open('Numbers.txt', 'w')
numb = ('1, 2 ,3 , 4 , 5')
f.writelines(numb)


#106
f = open('Names.txt', 'w')
names = ('Luis \n Alexander \n Allison \n Ibou \n Darwin' )
f.write(names)


#107
f = open('Names.txt')
print(f.read())


#108
f = open('Names.txt', 'a')
f.write('\nJoe')
print(f.read)
f = open('Names.txt')
print(f.read())


#109
menu = input('1) Create a new file\n2) Display the file\n3) Add a new item to the file\nMake a selection 1, 2 or 3: ')
if menu == '1':
    ask_sub = input("Enter a subject: ")
    f = open('Subject.txt', 'w')
    f.write(ask_sub)
elif menu == '2':
    f = open('Subject.txt')
    print(f.read())
elif menu == '3':
    new_subj = input("enter a new subject and save the file, and display the entire contents of the file: ")
    f = open('Subject.txt', 'a')
    f.write('\n'+ new_subj)
    f = open('Subject.txt')
    print(f.read())
else:
    print("Error!  you should choose only 1, 2 or 3 .")


#110
f = open('Names.txt')
print(f.read())
choose = input("Type one of them:  ")
if choose == 'luis':
    f = open('Names2.txt', 'w')
    f.write('Alexander\nAllison\nIbou\nDarwin\nJoe')
elif choose == 'alexander':
    f = open('Names2.txt', 'w')
    f.write('Luis\nAllison\nIbou\nDarwin\nJoe')
elif choose == 'allison':
    f = open('Names2.txt', 'w')
    f.write('Luis\nAlexander\nIbou\nDarwin\nJoe')
elif choose == 'ibou':
    f = open('Names2.txt', 'w')
    f.write('Luis\nAlexander\nAlisson\nDarwin\nJoe')
elif choose == 'darwin':
    f = open('Names2.txt', 'w')
    f.write('Luis\nAlexander\nAllison\nIbou\nJoe')
elif choose == 'joe':
    f = open('Names2.txt', 'w')
    f.write('Luis\nAlexander\nAlisson\nDarwin\nIbou')
else:
    print("Error, please type correct name!")