def regressiva (i) :
    print (i)
    if i <= 1:
        return 1
    else:
        regressiva(i-1)
    

def fat (x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)

print(fat(5))

#recursao: uma funcao que chama a si mesma
#util para problemas que podem ser divididos em subproblemas
#exemplo: fatorial de um numero
#porem a recursao pode ser ineficiente para problemas grandes ocupa muita memoria
#e tempo de processamento
#exemplo: fatorial de 1000
