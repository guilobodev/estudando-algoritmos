def pesquisa_binaria (lista, item): #funçao para passar os parametros da lista e o item que queremos achar
    baixo = 0 
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        if chute < item:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]



print (pesquisa_binaria(minha_lista, 1))
print (pesquisa_binaria(minha_lista, -1))

