phrase = str(input("Say to me some beautiful words: "))
"""
Esto lo que hace basicamente es sustituir '' iterando en cada caracter (char) existente dentro de my_string
"""
def disemvowel(my_string):
    return ''.join(char for char in my_string if char.lower() not in 'aeiou')

print(disemvowel(f"{phrase}"))

#filter, map .replace

print("hola".split())