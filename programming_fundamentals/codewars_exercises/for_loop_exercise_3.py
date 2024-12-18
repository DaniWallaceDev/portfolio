def get_middle(s):
    mid_large= len(s)//2
    if len(s)%2==0:
        mid_char = s[mid_large-1:mid_large + 1]
    else:
        mid_char = s[mid_large]
    return mid_char

get_middle("adios")

