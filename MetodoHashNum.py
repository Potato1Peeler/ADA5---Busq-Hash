def ordenar_hash(lista):
    rango = max(lista) + 1  
    tabla_hash = [[] for _ in range(rango)]

    for numero in lista:
        tabla_hash[numero].append(numero) 

    lista_ordenada = []

    for cubeta in tabla_hash:
        lista_ordenada.extend(cubeta) 
        
    return lista_ordenada

datos = [50, 23, 75, 12, 5, 85, 32]
resultado = ordenar_hash(datos)
print("Lista ordenada:", resultado)
