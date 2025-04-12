# Este es mi primer ejercicio de pytho
# Hola mundo EJ1
#print("¡Hola mundo"); 
# Completado con éxito



#Ejercicio 2 
# Es un almacenamiento en una variable 
#saludo= "¡Hola mundo!"
#print("\n\nesto es un saludo guardado en una variable\n" , saludo)  # se utiliza el \n como salto de linea

#Ejercicio 3
#Introducción de nombre por consola y luego mostrar el nombre

#name= input("¿Cuál es tu nombre? \n")
#print("¡Hola!\n", name, "\nEs un gusto tenerte acá¿") 
# Mostramos la variable que preguntamos hace un rato 


#Ejericicio 4
# Mostrar resultado de la operación
#print(((3+2)/(2*5))**2)


#Ejercicio 5
#Horas de trabajo y pago por horas de trabajo 
#Hour= float(input("¿Cuántas horas trabaja?\n"))

#if Hour<0: #Validar ingreso de números positivos para horas
 #   print("Ingrese valores positivos")
  #  while Hour<0: 
   #     Hour=float(input("¿Cuántas horas trabaja?\n"))
          
#pay= float(input("¿Cuánto le pagan por hora de trabajo?\n"))

#if pay<0: #Validar ingreso de números positivos para pago 
 #   print("Ingrese valores positivos")
  #  while pay<0:
   #     pay=float(input("¿Cuánto le pagan por hora de trabajo?\n"))
        
#cash= Hour * pay # guardar producto de los valores ingresados
#print("Usted debe recibir $",cash,".00") # Mostrar cash para la paga


#Ejercicio 6
# Ejericico de serie aritmética
#print("HOLA VAMOS A REALIZAR UNA SERIE\n LA SERIE ES\n (n(n+1))/2")
#n= int(input("Ingrese el número final de la serie: \t"))# Ingreso del valor de la serie
#ResultadoSerie= (n*(n+1))/2 #Resolución de la serie
#print("EL RESULTADO FINAL DE LA SERIE ES\t", ResultadoSerie) #Resultado de la serie

#Ejericicio 7 
#Ejericio de imc 
Peso= float(input("¿Ingrese su peso corporal? \n"))
if Peso<0:
    print("VALOR INCORRECTO")
    while Peso<0: 
        Peso= float(input("¿Ingrese su peso corporal? \n"))

Talla=float(input("¿Ingrese su estatura?\n"))
if Talla<0: 
    print("VALOR INCORRECTO")
    while Talla<0: 
        Talla=float(input("¿Ingrese su estatura?(en cm)\n"))

imc= Peso/(((Talla*0.01))**2)
print("Su imc es ", imc)
if imc<18.5:
    print("Está bajo de peso")
elif imc>18.5 and imc<24.9: 
    print("Está en un peso saludable")
elif imc>25 and imc<29.9:
    print("Está en sobrepeso")
else: 
    print("TIENE SOBREPESO")
        





