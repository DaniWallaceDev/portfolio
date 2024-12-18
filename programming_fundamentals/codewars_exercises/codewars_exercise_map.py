#DNA exercise from codewars

def DNA_strand(dna_chain):
    dna = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C"
    }
    selector= map(lambda char:dna[char],dna_chain)
    print(type(selector))
    return "".join(selector)

"""
¿Porque map devuelve una direccion de memoria y ha de ser transformado? 
La clase map se transforma para ser devuelto como string?
"""

print(DNA_strand("GTAT"))
#¿Se pueden devolver keys de values a la inversa?

"""
Ejemplos:
Ejemplo de comprension de listas, buscar:
            pairs = {'A':'T','T':'A','C':'G','G':'C'}
            def DNA_strand(dna):
                return ''.join([pairs[x] for x in dna])
"""


