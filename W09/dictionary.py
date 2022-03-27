
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
print()

del tel['sape']
tel['ire'] = 3127
print(tel)
print()
print(sorted(tel)) # gives only the colum name
print()
'guido' in tel
'jack' not in tel
print()

cc = dict([('sape', 4123),('rie', 3922), ('dfdf', 4883)])
print(cc)
print()

# item() method
kn = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in kn.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']): # gives the index number
    print(i ,v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers): # zip(): pair the list up
    print('What is your {}? It is {}'.format(q, a))

for i in reversed(range(1, 10 ,2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear','orange','banana']
for i in sorted(set(basket)):
    print(i)

print()
print()
phone_number = {}
phone_number["Jenny"] = "(555) 856 - 3433"
print(phone_number["Jenny"])

print()
print()
capitals = {} # making a set
capitals["Idaho"] = "Boise"
capitals["Utah"] = "Salt Lake City"
capitals['Calfornia'] = "Sacramento"

state = input("Enter a state name: ")
capital = capitals[state]
print("The capital of {} is {}".format(state, capital))
"""

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))



education = {} # or dict()

with open("census.csv", "r") as file_in:
    next(file_in)
    for line in file_in:
        result = line.split(",")
        edu = result[3]
        if edu in education:
            education[edu] += 1 # education[edu] = velue of edu
        else:
            education[edu] = 1 # adding edu name and it is for the empty case in the begining

# so education[edu] is doing two things 1)add a column if it is not in a dictionary 2) calling the exist column's value

# print out all key and values in the dictionary
# The itmes() function returns a list of (key, value) tuples
for edu, count in education.items(): # edu and count is in order
    print("{:5} -- {}".format(count, edu)) #{:5} sets the width to 5

print(education)
"""