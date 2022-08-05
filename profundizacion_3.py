# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''
print('ingrese la primer temperatura')
tempreratura_1 = int(input)
print('infgrese la temperatura 2')
tempreratura_2 =int(input)
print('ingrese la tercer temperatura')
tempreratura_3 = int(input)

if (tempreratura_1 > tempreratura_2 ) and (tempreratura_1 > tempreratura_3 ):
    print ('la tempreatura mas alta es:', temperatura_1)
elif (tempreratura_1 < tempreratura_2 ) and (tempreratura_1 < tempreratura_3 ):
    print('la temperatura mas baja es:', tempreratura_1)
else:
    print('la temperatura intermedia es:', temperatura_1)

if (tempreratura_2 > tempreratura_1 ) and (tempreratura_2 > tempreratura_3 ):
    print ('la tempreatura mas alta es:', temperatura_2)
elif (tempreratura_2 < tempreratura_1 ) and (tempreratura_2 < tempreratura_3 ):
    print('la temperatura mas baja es:', tempreratura_2)
else:
    print('la temperatura intermedia es:', temperatura_2)

if (tempreratura_3 > tempreratura_2 ) and (tempreratura_3 > tempreratura_1 ):
    print ('la tempreatura mas alta es:', temperatura_3)
elif (tempreratura_3 < tempreratura_2 ) and (tempreratura_3 < tempreratura_1 ):
    print('la temperatura mas baja es:', tempreratura_3)
else:
    print('la temperatura intermedia es:', temperatura_3)

promedio = tempreratura_1 +tempreratura_2 + tempreratura_3 % 3 

print('el promedio de las tres temperaturas es:', promedio)

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
