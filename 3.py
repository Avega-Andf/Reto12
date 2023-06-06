# 50 palabras


file = open('texto.txt', "r")

dicpalabras = {} # Se crea un diccionario en donde se guardaran todas las palabras del texto
for line in file: # Por cada linea en el archivo
    linea = line.split() # Se crea un lista por cada linea, en donde saldran todas las palabras separadas por espacios
    for palabra in linea: # Por cada palabra de la lista
        if palabra in dicpalabras: # Si la palabra esta en el diccionario, el valor de la llave aumenta en uno 
            dicpalabras[palabra] += 1
        else:
            dicpalabras[palabra] = 1 # Si no esta en el diccionario, la palabra se agrega en el diccionario con el valor de uno

listadepalabras = list(dicpalabras.items()) # Se convierte el diccionario en un lista de tuplas
print("lista de palabras con la cantidad de veces que aparece: ", listadepalabras)
listadepalabras.sort(key=lambda x: x[1], reverse=True) # Funcion lamba para ordenar de mayor a menor, ordena segun el segundo elemento del diccionario
c50palabras = listadepalabras[:50] # Improme hasta el valor anterior al 50
print("Palabras que mas aparecen:")
for palabra, veces in c50palabras:# se imprime las 50 palabras y la cantidad de veces que salio, de la lista c50palabras 
    print(palabra,":",veces)
    
file.close()