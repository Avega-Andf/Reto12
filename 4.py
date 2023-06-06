def Correo(linea):
    # Encontrar la posición de inicio de la dirección de correo
    inicio = linea.find('from ') + 5
    # Encontrar la posición de fin de la dirección de correo
    fin = linea.find(' ', inicio)
    # Extraer la dirección de correo de la línea
    correo = linea[inicio:fin]
    return correo

def Destinatarios(archivo):
    # Crear un diccionario para almacenar los destinatarios y la cantidad de veces que aparecen
    destinatarios = {}
    # Abrir el archivo para leerlo
    file = open(archivo, "r")
    # Leer cada línea del archivo
    for linea in file:
        # Convertir la línea a minúsculas y eliminar espacios en blanco al inicio y al final
        linea = linea.lower().strip()
        # Verificar si la línea comienza con 'received:'
        if linea.startswith('received:'):
            # Obtener la dirección de correo de la línea utilizando la función Correo()
            correo = Correo(linea)
            # Verificar si se obtuvo una dirección de correo válida
            if correo:
                # Incrementar la cantidad de veces que aparece el correo en el diccionario
                destinatarios[correo] = destinatarios.get(correo, 0) + 1 # Si no existia regresa el valor de cero y se le suma uno,
                # si existe, se le suma la llave que tiene el diccionario + 1, porque se encontro un nuevo mensaje 

    return destinatarios


if __name__ == "__main__":
    # Nombre del archivo
    archivo = 'texto.txt'
    # Obtener los destinatarios y la cantidad de veces que aparecen utilizando la función Destinatarios()
    resultados = Destinatarios(archivo)
    # Imprimir los resultados
    for correo, cantidad in resultados.items():
        print(correo, ":" , cantidad)
