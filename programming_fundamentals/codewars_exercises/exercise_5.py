"""
Que pasaría si quisiera pedir al usuario un str input pero yo necesitara hacer el calculo con eso?
"""
year = input("What year are we in?: ")
print(type(year))
year = int(year)
print(year)

# Como hacer con condicionales que si el usuario mete un valor no conversible a int devuelva un error y probar con try except

# year = int(year)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")