
"""
def descending_order(num):
    num_list= [x for x in str(num)]
    num_list=sorted(num_list, reverse=True)
    num_list="".join(num_list)
    return int(num_list)
print(descending_order(2649))
1. Encuentra el numero maximo de una lista sin sort
for i in range(0, len(list)):
    print(i)
    for j in range(i+1, len(list)):
        print(i)
        if list[i] >= list[j]:
            list[i], list[j] = list[j],list[i]
"""
list=[100,2,9,400,5]
print("Original List:", list)
"""
EN ESTE CASO USAMOS UNA VARIABLE TEMPORAL PARA RETENER EL VALOR DE LIST[I]
POSTERIORMENTE ESTE VALOR SE ASIGNARA A LIST[J] UNA VEZ QUE LIST[I] TOMA EL VALOR ANTERIOR DE LIST[J]

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] >= list[j]:
            x = list[i]
            list[i] = list[j]
            list[j] = x
print("Sorted list:", list)
"""

"""
EN ESTE CASO NO SE USA LA VARIABLE TEMPORAL Y PARA ELLO EN SU LUGAR SE VA ASIGNANDO EN CADA ITERACION
UN VALOR DE LIST[J] A LIST[I] SIEMPRE QUE ESTA CUMPLA CON LA CONDICION Y DE ESTA FORMA NO SE PIERDE EL VALOR
ADEMAS DE ESTO LA LISTA SE VA ORDENANDO MODIFICANDO LA VARIABLE LIST CON CADA ITERACION DEL SEGUNDO FOR

for i in range(0,len(list)):
#    print("i",i,"valor i", list[i])
    for j in range(i+1,len(list)):
#        print("i:",i,"valor i:", list[i],"j:",j,"valor j:",list[j])
        if list[i] >= list[j]:
            list[i], list[j] = list[j], list[i]
print("Sorted list:", list)
"""

