def ordenar_hash_cadenas(lista):
    longitud_maxima = max(len(palabra) for palabra in lista)  
    tabla_hash = [[] for _ in range(longitud_maxima + 1)]

    for palabra in lista:
        indice = len(palabra)
        tabla_hash[indice].append(palabra) 

    lista_ordenada = []

    for cubeta in tabla_hash:
        cubeta.sort()  
        lista_ordenada.extend(cubeta)  
        
    return lista_ordenada

palabras = ["casa", "gato", "elefante", "yo", "hola", "sol"]
resultado = ordenar_hash_cadenas(palabras)
print("Lista ordenada:", resultado)
