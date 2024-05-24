#1
empty_tuple = ()
print(type(empty_tuple))


#2
diff_tuple = (11, 'Diaz', 5.0, False)
print(type(diff_tuple))
print(diff_tuple)


#3 
one_data = ('Raguel',)
print(type(one_data))
print(one_data)


#4
tuples_ = (1, 2, 'salah',)
add_tup = list(tuples_)
add_tup.append('Cody Gakpo')
tuples_ = tuple(add_tup)
print(tuples_)
print(type(tuples_))


#5
many = (5, 'Konate', True)
convert = list(many)
print(convert)
print(type(convert))


#6
some_tuples = ('red', 'green', 'blue', 'yellow', 'purple', 'orange', 'white', 'black')
print(some_tuples[3])
print(some_tuples[-4])
print(type(some_tuples))


#7
lfc = ('trent', 'vvd', 'mac allister', 'vvd', 'robertson', 'vvd')
myset = set(lfc)
print(len(myset))


#8
coach = ('Klopp', 'Pep', 'Morinho')
l = list(coach)
l.remove('Morinho')
coach = tuple(l)
print(type(coach))
print(coach)


#9
coach = ('Klopp', 'Pep', 'Morinho')
del coach


#10
ind = ('Y', 'O', 'U','', 'L', 'L','', 'N', 'E', 'v', 'E', 'R','', 'W', 'A', 'L', 'K','', 'A', 'L', 'O', 'N', 'E' )
print(ind[ : :7])


#10 

tupp = ('I', 'N', 'D', 'E', 'X' '', 'T', 'U', 'P', 'L', 'E')
index = tupp.index('D')
print(index)


#11
tupls = [(), (), (''), ('d'), ('h')]
for i in tupls:
    if i == ():
        tupls.remove(i)
print(tupls)






#11
tupls = [(), (), (''), ('d'), ('h')]
tupls.pop(0)
tupls.pop(0)
print(tupls)




#12
t = (4, 3, 2, 2, -1, 18)
sum = 1
for i in t:
    sum = i * sum
print(sum)



#12 
t = (2, 4, 8, 8, 3, 2, 9)
sum = 1
for i in t:
    sum = i * sum
print(sum)


