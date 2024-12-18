print("Hello World")

#VARIABLES
my_variable = "There!"
my_integer_variable = 1
x = "Hola"
y = "Holita"
w = 2
z = 3

#OPERATORS
print("Hello " + my_variable)
print(w+z)
print(w*z)
print(w-z)
print(w/z)
print(w//z)
print(w**z)
print(w%z)
#print(x/y) why? Because characters are not comparable beetwen

#LOGICAL OPERATORS
string = "example1"
string2 = "example2"
integer = 1
integer2 = 2
print(string == string2)
print(string != string2)
print(integer == integer2)
print(integer != integer2)
print(integer < integer2)
"""
These logical operator show you how counting the number of characters
that each string have u can say if the operator are true or false
"""

# ***ITERATORS***
# LISTS
my_list = [] # empty list
my_list = ["tomatoes", "potatoes"] # a list can have all types inside!

my_list = [[], []] # a list can have a list inside!

my_list = [1,2,3]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[0]+my_list[2])
print(my_list[2]+my_list[2])
print(my_list[2]==my_list[2])
print(my_list[2]!=my_list[2])
print(my_list[0]<my_list[2])
print(my_list[0]>my_list[2])

"""
print(my_list[3]) 
Executing this gonna give u an error because of list range that is beetween 0 to 2
There are 3 elements in this case integers but from position 0 to position 2
"""
my_list = [1, 2, 3, "potatoes", "tomatoes"]
print(my_list)
"""
In the normal flow of the code u can see how my_list value change to [1, 2, 3, "potatoes", "tomatoes"]
Because u equal my_list to these elements at the last line of code
"""

"""
***Can you tell how we would define a new element inside the existing list?***
Easy you can asign an element to a position using the method .append()
or method .insert(3,"")
or method .extend([4, 5]) to insert some elements not only one
or using the same logic used before these comment like using variables => my_list[3] = 2
"""
my_list.append(4)
print(my_list)
my_list.insert(3, 'insertado donde quiero')
my_list[3] = 2
print(my_list)

# DICTIONARIES
my_dictionary = {}
my_dictionary = {
    "list": [3,2,1,'hola'], #differences between using'' or ""?
    "variable": my_list,
    "int": 1
}
print(my_dictionary)
print(my_dictionary["list"])
print(my_dictionary["variable"])
print(my_dictionary["int"])
# print(my_dictionary["fourth"])
"""
U can't run the last print because u're trying to access to a none or undefined key of a dictionary
of course that key haven't any value in it
"""
my_dictionary["fourth"]= 2
print(my_dictionary["fourth"])
print(my_dictionary)
"""
By these 2 ways u can asign a new key and value to an existing dictionary in python
"""
my_dictionary.update({'five': 3})
print(my_dictionary)

