def encontrarValor(array):
    if len(array) == 1:
        return array[0]
    else:  
        if array[0] > encontrarValor(array[1:]):
            return array[0]
        else:
            return encontrarValor(array[1:])
        
 



   
print(encontrarValor([20,40,90,78,80]))