def soma (array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + soma(array[1:])

print (soma([1,2,3,4,5]))