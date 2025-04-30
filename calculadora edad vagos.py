
print ("======================================")
print ("CALCULADORA DE EDAD PARA VAGOS/AS")
print ("======================================")
# Solicitar el año actual
año_actual_str = input("Introduce el año actual: ")
# Convertir el tipo string en integer
año_actual= int(año_actual_str)
# Solicitar año de nacimiento
año_nacimiento_str= input("Introduce el año en que naciste: ")
#Convertir el tipo de año de nacimiento de string a integer
año_nacimiento= int(año_nacimiento_str)
#Calculo de la edad con operadores
edad = año_actual - año_nacimiento 
# Condicionales para mostrar mensajes personalizados segun rango de edad
if edad > 25 and  edad < 31:
   print ("Los treinta son los nuevos veinte, ¡ya queda menos para tener tu propia casa!")
elif edad < 1:
   print ("Ups, lo siento pero para saber tu edad mejor preguntale a tu madre, el tema de los meses no lo controlo bien")
elif edad > 2 and edad < 6:
   print ("¿Pero acaso sabes leer? ¡mejor vete a jugar al parque!")
elif edad > 6 and edad < 12:
   print ("¿Te sabes ya las tablas de multiplicar? pues multiplicate por cero ;P")
elif edad > 12 and edad < 20:
   print ("Vales más de lo que los demás te demuestran, quierete mucho")
elif edad > 35:
   print ("¡Entiendo que me hayas usado para saber tu edad, esto ya son calculos mayores!")
#Mostrar edad 
print ("Tienes", edad, "años :)") 



