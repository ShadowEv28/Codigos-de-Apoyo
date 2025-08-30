#Print es un comando bastante simple realmente, aunque cuenta con varias opciones interesantes.
print("1) Hola Mundo") #Este es un print simple que ya todo deben conocer, es facil de entender y bastante utilizado.
print(f"2) Hola") #Agregar una f antes de las comillas permite poder utilizar variables de forma mas simple y rapida.
palabra = "Mundo"
print(f"3) Hola {palabra}") #Como pueden ver aqui, pude utilizar la variable "palabra" sin la neceidad de salir de las comillas, aunque utilizar la f tambien sirve para hacer calculos entre variables de forma mas rapida.
edad = 21
año = 2025
print(f"4) Hola, tengo {edad} y naci el {año - edad}") #Como ven en el codigo, pude calcular el año de nacimiento de forma rapida solo con 2 variables dentro del print y sin necesidad de una tercera variable.
print("5) Hola \nMundo") #El comando \n sirve para hacer un salto de linea dentro del print.
print("6) Hola \tMundo") #El comando \t sirve para hacer una tabulacion dentro del print.
print("7) Hola \"Mundo\"") #El comando \" sirve para poder utilizar comillas dentro de un print que ya esta entre comillas.
print("8) Hola \'Mundo\'") #El comando \' sirve para poder utilizar comillas simples dentro de un print que ya esta entre comillas dobles.
print("9) Hola \\Mundo") #El comando \\ sirve para poder utilizar una barra invertida dentro de un print que ya esta entre comillas.
print("10) Hola Mundo", end=" :)") #El comando end sirve para cambiar el final del print, en este caso en vez de hacer un salto de linea, termina con una carita feliz.
print("11) Hola Mundo") #Como pueden ver, el print anterior no hizo un salto de linea, sino que termino con una carita feliz.
print("12) Hola Mundo", sep="-") #El comando sep sirve para cambiar el separador entre varios elementos dentro de un print, en este caso en vez de un espacio, utiliza un guion.
print("13) Hola", "Mundo", sep="*") #Como pueden ver, el print anterior utilizo un asterisco como separador entre las dos palabras.
print("14) Hola", "Mundo", sep="***") #Como pueden ver, el print anterior utilizo tres asteriscos como separador entre las dos palabras.
print("15) Hola", "Mundo", sep="\n") #Como pueden ver, el print anterior utilizo un salto de linea como separador entre las dos palabras.
print("16) Hola", "Mundo", sep="\t") #Como pueden ver, el print anterior utilizo una tabulacion como separador entre las dos palabras.
print("17) Hola", "Mundo", sep=" - ") #Como pueden ver, el print anterior utilizo un espacio, un guion y otro espacio como separador entre las dos palabras.
print("18) Hola", "Mundo", sep=" :) ") #Como pueden ver, el print anterior utilizo una carita feliz con espacios como separador entre las dos palabras.
