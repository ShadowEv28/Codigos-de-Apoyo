#En cualquier lenguaje de programacion las variables son algo bastante comun y utilizado para guardar datos dentro del codigo.
#En python las variables existentes son: String, Int, Float y Bool
#Aunque en realidad hay bastantes variables mas, estas son las mas comunes.
Variable_String = "Hola" #Las variables String son variables de texto, estas variables solo almacenaran palabras.
print(Variable_String) #Como pueden ver al imprimir la variable, esta mostrara la palabra "Hola", las variables string no se pueden supar como numeros, pero pueden unirse
print(Variable_String + Variable_String) #Como ven al imprimir la variable enseña el texto 2 veces y juntos.
Variable_Int = 20 #Las variables tipo int son Variables que almacenan solo numeros enteros.
print(Variable_Int) #Al imprimir variables Int esta arrojara el valor del numero, estas variables si pueden sumarse y se pueden hacer calculos matematicos con estas.
print(Variable_Int + Variable_Int) #Al sumar dos variables Int es como sumar los valores de la variable en una calculadora.
#print(Variable_Int + Variable_String) #Al intentar sumar cualquier cosa que no sea un String con un String, este dara error y terminara el codigo. Si deseas comprobarlo, puedes borrar el # antes del print y ejecutar el codigo.
print(Variable_Int * 10) #La variable Int al ser un numero, este puede ser manipulado como si fuera una calculadora.
Variable_Float = 0.2 #Las variables Float son variables que pueden almacenar numeros enteros y decimales.
print(Variable_Float) #Al imprimir variables float es igual que las demas, imprime el valor directo de la variable.
print(Variable_Float + Variable_Float) #Al igual que una variable Int, estas variables se pueden sumar y hacer calculos matematicos con estas variables.
print(Variable_Float + Variable_Int) #Al sumar una variable Float con una Int se sumaran los valores como un numero.
print(Variable_Float * 10) #Como la variable Int, estas puden ser manipuladas como en una calculadora sin ningun problema.
Variable_Bool = True #Una variable Bool o Boolean es una variable que solo puede ser Verdadera(True) o Falsa(False), estos valores siempre deben estar escritos en ingles para funcionar.
print(Variable_Bool) #Al igual que cualquier variable impresa, esta mostrara su valor.
print(Variable_Bool + Variable_Float + Variable_Int) #Al sumar una variable Bool con variables numericas, esta sumara 1 ya que se puede interpretar que una variable True es igual a 1 mientras que False es igual a 0.
#Ahora enseñaremos como convertir una variable a otra.
#Para convertir una variable a otra podemos hacerlo con escribir el tipo de variable que queremos convertirla, poner parentesis junto a esta y dentro del parentesis poner el valor que queremos canviar.
#Para cada variable se debe usar lo siguiente: String = str; Int = int; Bool/Boolean = bool; Float = float.
strbool = str(Variable_Bool) #Aqui convertimos un bool a String
strint = str(Variable_Int) #Aqui convertimos un Int a String
strfloat = str(Variable_Float) #Aqui convertimos un Float a String
print(strbool + strfloat + strint) #Como ven aqui los valores se juntan unos a otros ya que todos son String ahora, si hubieramos intentado esto antes los valores simplemente se hubieran sumado y daria 21.2
Variable_List = [] #Las variables List son variables que pueden almacenar multiples valores y de todo tipo.
Variable_List.append("Dato 1") #En las variables List se pueden añadir valores usando ".append()"

