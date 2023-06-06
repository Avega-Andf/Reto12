# Fecha y numero de mensajes
def mensajesdiarios(texto: str) -> dict:
    recibidos = []  # Lista de palabras del texto que contienen la la fecha.
    palabras = texto.split()  # Lista de palabras del texto
    segmento = []  # Lista temporal para almacenar cada fecha encontrada
    
    for palabra in palabras:  # Bucle for para iterar sobre las palabras en el texto
        if palabra == "Received:":  # Verificar si la palabra actual es "Received:"
            segmento = [palabra]  # Crear un nuevo elemento de segmento con la palabra actual
        elif "-0500" in palabra or "(GMT)" in palabra:  # Verificar si se encontró el final de un segmento
            if segmento:  # Verificar si hay palabras en el segmento actual antes de agregarlo
                recibidos.append(segmento) # Agrega el segmento a la lista recibidos
            segmento = []  # Reiniciar la lista para el próximo conjunto de palabras
        elif segmento:  # Verificar si hay un segmento actual en el que agregar la palabra
            segmento.append(palabra)
    
    mensajes_por_dia = {}  # Se crea un diccionario para almacenar el día y el número de mensajes enviados.
    for segmento in recibidos:
        indice = segmento.index('Jan')  # Índice de la palabra "Jan".
        dia = int(segmento[indice - 1])  # Se extrae el día en función del índice de "Jan".
        if dia in mensajes_por_dia:  # Bloque de código para llenar el diccionario.
            mensajes_por_dia[dia] += 1 # Si ya este la llave, el valor de la llave aumenta uno
        else:
            mensajes_por_dia[dia] = 1 # si no esta se asigna a la llave el valor de uno

    return mensajes_por_dia

if __name__ == "__main__":
    file = open('texto.txt', "r")
    for line in file:
        numeros_dia = mensajesdiarios(file.read())
        for dia in numeros_dia: # Iteracion para sacar el dia y la cantidad de mensajes que se enviaron en este
            print("Se enviaron", numeros_dia[dia] , " mensajes el" ,dia,  "de enero del 2008")