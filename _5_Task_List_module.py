#1 create empty list
lfc = []

#2 create list 5 and more elements
lfc = ['salah' , 'diaz', 'gakpo', 'vvd', ' alisson', 'trent']
print(lfc)


#3 finf your list length
lfc = ['salah' , 'diaz', 'gakpo', 'vvd', 'alisson', 'trent']
print(len(lfc))


#4 print first , middle and last list of element
lfc = ['salah' , 'diaz', 'gakpo', 'vvd', 'alisson', 'trent', 'mac allister']
print(lfc[0])
print(lfc[3])
print(lfc[6])


#5 create list named 'mixed_data_types', insert your name, age, height, relationship, address
mixed_data_types = ['Gela', '27', '193', 'single', 'godziasvili street']
print(mixed_data_types)


#6 create list variable named 'it_companies' and asign starting value
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 

#7
print(it_companies)

#8 
print(len(it_companies))

#9 print first , middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])


#10 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[2] = 'Dell'
print(it_companies)


#11
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.insert(2, 'IBM')
print(it_companies)


#12
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']
it_companies.insert(3, 'IBM')
print(it_companies)


#13
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
it_companies[1] = 'GOOGLE'
print(it_companies)


#14 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
if "Google" in it_companies:
    print("yes it is.")


#15
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)


#16
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.reverse()
print(it_companies)


#17
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.remove('Facebook')
it_companies.remove('Google')
it_companies.remove('Microsoft')
print(it_companies)


#18
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.remove('IBM')
it_companies.remove('Oracle')
it_companies.remove('Amazon')
print(it_companies)


#19
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(3)
print(it_companies)


#20
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
print(it_companies)


#21
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(3)
print(it_companies)


#22
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop()
print(it_companies)


#23
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)


#24
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies
print(it_companies)


#1
numb = [7, 9, 11]
print(sum(numb))



#2
numb = [3, 1, 2, 3]
sum = 1
for i in numb:
    sum = i * sum
print(sum)





#3
numb = [2, -5, 11, -4]
print(max(numb))


#4
numb = [2, -5, 11, -4]
print(min(numb))



#5 
lfc = ['Salah', 'Diaz', 'Nunez']
if len(lfc) == 0:
    print("Empty")
else:
    print('list is not empty')




#6
numb = [2, -5, 11, -4]
numb_copy = numb.copy()
print(numb_copy)



#7 
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.remove('Red')
color.remove('Pink')
color.remove('Yellow')
print(color)



#8 
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
index = color.index('Green')
print(index)
