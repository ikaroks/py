def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    lista_ordenada = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1
    
    lista_ordenada.extend(esquerda[i:])
    lista_ordenada.extend(direita[j:])
    
    return lista_ordenada


lista = [9, 3, 5, 2, 1, 4, 7, 0]
print("Lista original:", lista)
print("Lista ordenada:", merge_sort(lista))