#exemplo de codigo do livro, para ordenar um array


#funcao que busca o menor elemento de um array
# econtra o indice de menor elemento do array e o retorna
def buscaMenor (array):
    menor =  array[0]
    menor_indice = 0
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i 
    return menor_indice




def ordenacaoPorSelecao(array):
    novoArr = []
    for i in range(len(array)):
        menor = buscaMenor(array)
        #pop remove o elemento do array
        #e o retorna para ser adicionado no novo array
        
        novoArr.append(array.pop(menor))
    return novoArr

print (ordenacaoPorSelecao([4,3,7,9,1,3]))
    
#exemplo : [4,3,7,9,1,3]
#menor = 1 e indice = 4
#novoArr = [1]
#array = [4,3,7,9,3]
#menor = 3 e indice = 1
#novoArr = [1,3]
#array = [4,7,9]
#menor = 4 e indice = 0
#novoArr = [1,3,4]
#array = [7,9]
#menor = 7 e indice = 0
#novoArr = [1,3,4,7]
#array = [9]
#menor = 9 e indice = 0
#novoArr = [1,3,4,7,9]
#array = []
#fim