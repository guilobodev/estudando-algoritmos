def contar(array):
    indice = 0
    if len(array) == 0:
        return 0

    else:
        indice += 1
        return indice + contar(array[1:])


print(contar([1,2,4,5,6,7]))