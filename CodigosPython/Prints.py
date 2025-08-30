#Print es un comando bastante simple realmente, aunque cuenta con varias opciones interesantes.
print("1) Hola Mundo") #Este es un print simple que ya todo deben conocer, es facil de entender y bastante utilizado.
print(f"2) Hola") #Agregar una f antes de las comillas permite poder utilizar variables de forma mas simple y rapida.
palabra = "Mundo"
print(f"3) Hola {palabra}") #Como pueden ver aqui, pude utilizar la variable "palabra" sin la neceidad de salir de las comillas, aunque utilizar la f tambien sirve para hacer calculos entre variables de forma mas rapida.
edad = 21
año = 2025
print(f"4) Hola, tengo {edad} y naci el {año - edad}") #Como ven en el codigo, pude calcular el año de nacimiento de forma rapida solo con 2 variables dentro del print y sin necesidad de una tercera variable.
print("5) Hola \nMundo") #El comando \n hace un salto a la siguiente linea y imprime lo que esta despues del \n.
print("6) Hola \tMundo") #El comando \t sirve para hacer una tabulacion, esto se refiere a un espacio largo, puedes probarlo apretando "TAB" tu mismo.
print("7) Hola \"Mundo\"") #El comando \" sirve para poder utilizar comillas dentro de print.
print("8) Hola \'Mundo\'") #El comando \' sirve para poder utilizar comillas simples dentro del print.
print("9) Hola \\Mundo") #El comando \\ sirve para poder utilizar \ dentro del print.
print("10) Hola Mundo", end=" :)") #El comando end sirve para cambiar lo que seria el salto de linea, en este caso en vez de saltar a la siguiente linea, esta tendra una carita feliz y continuara en la misma linea.
print("Pueden ver que la linea no salto")
print("11) Hola","Mundo ", sep="-") #El comando sep sirve para separar los elementos dentro del print.
#Por ahora estos son comnados de pythons para print que son utiles y faciles.