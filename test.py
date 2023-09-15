import random

#Número random
num_random=random.randint(1,20)
print(num_random)

#Calculos básicos
print(2+2)
print(4*3)
print(10/2)
print(4-2)

#Mostrar en pantalla y escribir por teclado.
print("¿Cuál es tu nombre?")
#nombre=input()
#print("tu nombre es "+nombre)

#Mostrar una cadena de texto con el parametro end
print("Mi nombre es Beni", end="")
print("TOOO")

#Divide las palabras por cada espacio.
var_phrase="Mi mum cooks very well"
print(var_phrase.split())

'''
Delante de los dos puntos ignora las posiciones de la cadena y no los muestra.
Detrás de los dos puntos solamente muestra las posiciones indicadas empezando desde la izq a la derecha.
'''
palabra="palabra"
print(palabra[:0])
print(palabra[:1])
print(palabra[1:])
print(palabra[2:])