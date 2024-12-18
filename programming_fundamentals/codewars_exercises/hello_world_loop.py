lista = [
    {"preso121": ["hermano", "dame", "un", "segarro"]},
    {"presa121": ["me", "importa", "una", "mierda", "calvo"]},
    {"preso122": ["ramadan", "si", "haram", "no"]},
    {"presa122": ["os", "escuche", "peleando"]},

]

dictionary = {
    "121": [],
    "122": []
}

for i in range(0,len(lista)):
    keys=list(lista[i].keys())[0]
    keys=list(keys)[-3:]
    key="".join(keys)
    values = list(lista[i].values())[0]
    dictionary[key] = dictionary[key] + [" ".join(values)]
print(dictionary)

"""
for i in range(0,len(lista)):
    keys=list(lista[i].keys())
    values=list(lista[i].values())
    dictionary[keys[0]] = dictionary[keys[0]] + values
    for i in dictionary:
        print(i)
print(dictionary)
"""

















