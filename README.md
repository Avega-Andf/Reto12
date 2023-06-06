# Reto 12

### 1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

#### endswith
+ Verifica si una cadena termina con el sufijo especificado. Devuelve True si la cadena termina con el sufijo dado, de lo contrario, devuelve False. Por ejemplo:


<details><summary>codigo</summary><p>

``` python
word = "Hola mundo"
print(word.endswith("mundo"))  # True

```
</p></details></br>

#### startswith
+ Verifica si una cadena comienza con el prefijo especificado. Devuelve True si la cadena comienza con el prefijo dado, de lo contrario, devuelve False. Por ejemplo:


<details><summary>codigo</summary><p>

``` python
word = "Hola mundo"
print(word.startswith("Hola"))  # True

```
</p></details></br>

#### isalpha() 
+ Verifica si una cadena contiene solo letras alfabéticas. Devuelve True si la cadena es alfabética, es decir, si no contiene espacios en blanco ni caracteres especiales, de lo contrario, devuelve False. Por ejemplo:

<details><summary>codigo</summary><p>

``` python
word = "Hello"
print(word.isalpha())  # True
```
</p></details></br>

#### isalnum()
+ Verifica si una cadena contiene solo caracteres alfanuméricos. Devuelve True si la cadena es alfanumérica, es decir, si no contiene espacios en blanco ni caracteres especiales, de lo contrario, devuelve False. Por ejemplo:

<details><summary>codigo</summary><p>

``` python
word = "Hello123"
print(word.isalnum())  # True
```
</p></details></br>

#### isdigit() 
+ Verifica si una cadena contiene solo dígitos. Devuelve True si la cadena contiene solo caracteres numéricos, de lo contrario, devuelve False. Por ejemplo:


<details><summary>codigo</summary><p>

``` python
number = "123"
print(number.isdigit())  # True
```
</p></details></br>

#### isspace() 
+ Verifica si una cadena contiene solo espacios en blanco. Devuelve True si la cadena contiene solo espacios, tabulaciones o saltos de línea, de lo contrario, devuelve False. Por ejemplo:

<details><summary>codigo</summary><p>

``` python
whitespace = "    "
print(whitespace.isspace())  # True
```
</p></details></br>

#### istitle()
+ Verifica si una cadena sigue las reglas de capitalización de título. Devuelve True si la cadena tiene el primer carácter de cada palabra en mayúscula y el resto en minúscula, de lo contrario, devuelve False. Por ejemplo:

<details><summary>codigo</summary><p>

``` python
title = "This Is a Title"
print(title.istitle())  # True
```
</p></details></br>

#### islower() 
+ Verifica si todos los caracteres de una cadena están en minúsculas. Devuelve True si todos los caracteres son minúsculas, de lo contrario, devuelve False. Por ejemplo:


<details><summary>codigo</summary><p>

``` python
lowercase = "hello"
print(lowercase.islower())  # True
```
</p></details></br>

#### isupper() 
+ Verifica si todos los caracteres de una cadena están en mayúsculas. Devuelve True si todos los caracteres son mayúsculas, de lo contrario

<details><summary>codigo</summary><p>

``` python
upercase = "HELLO"
print(upercase.isupper())  # True

```
</p></details></br>



## Gracias por leer. 