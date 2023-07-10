from os import system
system ("cls")

platinium=120000
gold=80000
silver=50000





entradas = [True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True,
            True,True,True,True,True,True,True,True,True,True]
reservass = []
recaudacionn=[]
asistentes=[]
valorrr=0
rut=[]


valorentradas=[]


def mostrar_entradas(entradas):
    for i in range(len(entradas)):
        if entradas[i] == True:
            estado = "Disponible"
        else:
            estado = " X "
        print(f" {i + 1}: {estado}")

def reservar_entrada(rut, entradas, reservas):
    cantidad_entradas=int(input("Cantidad Entradas (1-3): "))

    reservas=[]
    print("""
        VALOR ENTRADAS:
        Platinium:  $120.000 (Asientos del 1 al 20)
        Gold:       $80.000 (Asientos del 21 al 50)
        Silver:     $50.000 (Asientos del 51 al 100)
        """)
    
    print("entradas disponibles:")
    for i in range(len(entradas)):
        if entradas[i]:
            print(f"entrada {i+1}")
    entrada = int(input("Ingrese el numero de la entrada que desea comprar: ")) -1
    if entradas[entrada]:
        entradas[entrada] = False
        reservas.append([rut, entrada])
        print("Reserva de entrada exitosa")
    else:
        print("Ya está reservada la entrada")
    if entrada >=1 <21:
        valor=cantidad_entradas*120000
    if entrada >=21 <=50:
        valor=cantidad_entradas*80000
    if entrada >=51 <=100:
        valor=cantidad_entradas*50000
        print("Valor total: ", valor)
        valor=valorentradas
    

def ver_recaudacion(reservas):
    for i in range(len(reservas)):
            print("Ganancia por entradas: ", valorentradas*i)
            recaudacionn.append(valorentradas)
            print("Ganancia Total:", recaudacionn)
            
while True:
    print("\n  CREATIVOS.CL")
    print("1. Comprar Entradas ") #reservar entrada
    print("2. Mostrar Ubicaciones disponibles ") #mostrar_entradas
    print("3. Ver listado de Asistentes ")
    print("4. Mostrar ganancias Totales ")#recaudacion
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion==1:
         #Reserva de entradas
        rut = int(input("Ingrese su RUT (sin puntos ni guion): "))
        nombre = (input("Ingrese su Nombre : "))
        apellido = (input("Ingrese su Apellido : "))
        reservar_entrada(rut,entradas,reservass)

    elif opcion==2:
        #Mostrar las entradas
        mostrar_entradas(entradas)
    elif opcion==3:
        #Ver lista de asistentes
        rut.sort()

    elif opcion==4:
        #Ver Recaudacion

        ver_recaudacion(reservass)
    elif opcion==5:
        print("Saliendo del sistema ""\n""Adios",nombre,apellido, "Fecha: 10/07/23")
        break
    else:
        print("Opción invalida. Intente de nuevo")


