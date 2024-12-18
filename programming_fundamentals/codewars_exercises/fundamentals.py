# EXERCISE 1
def double_int (n:int) -> int:
    return n*2

print(double_int(4))

# EXERCISE 2
def half_even_string (s:str) -> str:

    s=s[0:len(s)//2]
    return s

print(half_even_string("1234"))

# EXERCISE 3
def compare_int_len (n:int, name:str) -> str:
    if n > len(name):
        print("The number is larger")
    else:
        print("The name is larger")
compare_int_len(2,"paco")

dictionary = {
    "name": "Rick",
    "age": "10000",
    "power": "Infinite",
    "purpose": "Pass the butter"
}

def change_dict_values(d: dict) -> dict:
    d["name"]="Robot"
    d["age"]="Unknown"
    d["power"]=1
    return d
print(change_dict_values(dictionary))
"""
PASAR COMO ARGUMENTO CUALQUIER VARIABLE SOBRE LA QUE SE DESEA TRABAJAR
NUNCA USAR VARIABLES GLOBALES DENTRO DE FUNCIONES
JAMAS USAR EL PRINT EN EL RETURN, RETURN ES PARA LO QUE QUEREMOS QUE DEVUELVA A FUNCION NO PARA ANIDAR OTRA FUNCION
"""
def change_dict_values_to_same (d:dict) -> dict:
    d=dictionary
    for i in list(d.keys()):
        d[i] = "caca"
    return d
print(change_dict_values_to_same(dictionary))

"""
def gather_input() -> str:
    user_input = input()
    user_input = user_input.strip().lower()

    return user_input


def choose_action(user_input: str) -> str:
    if user_input == "say hi":
        return "hello there!"

    if user_input == "say goodbye":
        return "bye bye!"

    if user_input == "high five":
        return "heeeigh fiiieve!"

    if user_input == "break":
        return user_input


def print_output(output: str) -> None:
    print(f"\n *{output}* \n")


while True:
    user_input = gather_input()

    if user_input == "break":  # break the infinite loop with a break input
        break

    to_print = choose_action(user_input)
    print_output(to_print)
"""

class Dog:
    name = ""
    age = 0
    fur = "sasa"
    race = ""

    def __init__(self, name,age, fur, race):  # this method allows us to
        # pass arugments and change attributes of the instance when instanciating it
        self.name = name
        self.age = age
        self.fur = fur
        self.race = race

    def bark(self):
        print(f"{self.name} barks!")

    def __eq__(self, name):
        return self.name == name



pipo = Dog("Pipo",2,"brown","chihuahua")  # creating an instance of the class
west = Dog("West",5,"white", "pitbull")

print(pipo.name.__eq__(west.name))
print(pipo == west)
pipo.bark()
west.bark()

print([0,4,3,1,5].index(1))
