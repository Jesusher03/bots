
#Primero tenemos que hacer que salude

n = "si"


def menu():
    opcion = input("Menu \n1) Horarios \n2) Servicios \n3) Veterinarios \n4) Numero de contacto \n5) Otras preguntas \n") 
    while opcion not in ["1","2","3","4","5"]:
        opcion = input("No resconozco esa opcion. Intente de nuevo \n")
    return opcion

def seleccion_menu(opcion):
     
    if opcion== "1":
        print(horario())
    elif opcion == "2": 
        print(servicios())
    elif opcion == "3":
        print(veterinarios())
    elif opcion == "4":
        print(contacto())
    elif opcion == "5":
        print("Cual es su pregunta?")
    
def horario():
    print("Horarios")
    print("Lunes : 9:00 a.m. - 6:00 p.m.")
    print("Martes : 9:00 a.m. - 6:00 p.m.")
    print("Miercoles : 9:00 a.m. - 6:00 p.m.")
    print("Jueves : 9:00 a.m. - 6:00 p.m.")
    print("Viernes : 9:00 a.m. - 6:00 p.m.")
    print("Sabado : 9:00 a.m. - 4:00 p.m.")
    print("Domingo : Cerrado")

def servicios():
    print("Servicios")

    print(""" Consulta general \n Vacunación \n Desparasitación \n Esterilización y castración 
        \n Cirugías generales \n Cirugías de emergencia \n Hospitalización \n Laboratorio clínico 
        \n Análisis de sangre \n Radiografías \n Ultrasonido \n Odontología veterinaria \n Limpieza dental 
        \n Control de peso \n Planes de medicina preventiva \n Certificados de salud \n Microchip e identificación 
        \n Medicina interna \n Dermatología \n Cardiología \n Oncología \n Traumatología y ortopedia \n Eutanasia humanitaria 
        \n Peluquería y estética \n Baño antipulgas \n Corte de uñas \n Venta de medicamentos \n Venta de alimentos especializados 
        \n Asesoría nutricional""")
    
    cita = input("desea agendar una cita? si/no").lower()

    while cita not in ["si","no"]:
        cita = input("Por favor reponda con si o no \n").lower()
        
    if cita == "si":
        nombre = input("Cual es su nombre?")
        fecha = input("Para que fecha le gustaria agendar (dia/mes/año)")
        numero_celular = input("Cual es su numero de celular?")
    generar_cita = (f"Nombre: {nombre} Fecha: {fecha} Tel: {numero_celular}")

    with open("Cita.txt", "a") as archivo:
        archivo.write(generar_cita)

        

def contacto():
    print("Numeros de contacto")
    print("5421884321")
    print("5421884321")
    print("5421884321")

def veterinarios():
    print("Veterinarios")
    print("Dr. Carlos Mendoza \nDra. Laura Fernández \nDr. Andrés Ramírez")

def seguimiento():
    n = input("Quiere entrar a otra sección? Si o No").lower()

    while n != "si" and  n != "no":
        n = input("Por favor solo responda si o no? Si o No").lower() 
    return n

print("Hola Bienvenido!! \n A la Estetica canina Guau Guau \n Yo sere su anfritrion en este espacio digital")

#Despues que pregunte que necesita y que despligue las opciones

while n == "si":
 
    opcion = menu()
    seleccion_menu(opcion)
    n = seguimiento()
   

print("Nos vemos la en tu proxima visita")


#para que sea un ciclo preguntamos si quiere saber algo mas si no que se acabe el programa
