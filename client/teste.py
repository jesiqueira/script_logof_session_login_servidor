
def recursao(numero, lista):
    if numero == 0:
        print('Ultimo')
        return True
    else:
        continuar = int(input('continuar digite 1: '))
        if continuar == 1:
            print(lista[numero-1])
            del lista[numero-1]
            recursao(numero -1, lista)
        else:
            return False

lista = range(10)
ni = recursao(len(lista), lista)
