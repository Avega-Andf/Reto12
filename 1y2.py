file = open('texto.txt', "r") # Abre el archivo
# Inicia los contadores en cero
vocales: int = 0 
consonantes : int = 0
# Numero de vocales y consonantes
for line in file.readlines():
    line = line.lower().strip() # Vuelve todas las letras del texto en minusculas y elimina los espacios de de derecha a izquierda,
    # Se vuelve todo en minuscula, para facilitar la busqueda, y tener que buscar solo las vocales y consonantes minusculas
    a = line.count("a") # Busca cuantas veces sale la vocal "a" en el texto
    e = line.count("e")
    i = line.count("i")
    o = line.count("o")
    u = line.count("u")
    vocales += a + e + i + o + u # Luego de buscar cuantas veces salio cada vocal, suma la cantidad de veces de cada una
    b = line.count("b")
    c = line.count("c")
    d = line.count("d")
    f = line.count("f")
    g = line.count("g")
    h = line.count("h")
    j = line.count("j")
    k = line.count("k")
    l = line.count("l")
    m = line.count("m")
    n = line.count("n")
    p = line.count("p")
    q = line.count("q")
    r = line.count("r")
    s = line.count("s")
    t = line.count("t")
    v = line.count("v")
    w = line.count("w")
    x = line.count("x")
    y = line.count("y")
    z = line.count("z")
    consonantes += b + c + d + f + g + h + j + k + l + m + n + p + q + r + s + t + v + w + x + y + z # Luego de buscar cuantas veces salio cuda consonante, se suma
    
print("Cantidad de vocales: " + str(vocales)) # Imprime la cantidad de vocales
print("Cantidad de consonantes: " + str(consonantes)) # Imprime la cantidad de consonantes

file.close()
