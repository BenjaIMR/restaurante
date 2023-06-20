import numpy
import os
import time
import msvcrt


arreglo_restaurante = numpy.zeros((3,3),int)

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in (1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")    
        except:    
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def ver_restaurante():
    while True:
        print("\nVER SALÓN PRINCIPAL DEL RESTAURANTE\n")
        for x in range(3):
            print(f"Fila {x+1}:\t" , end=" ")
            for y in range(3):
                print(arreglo_restaurante [x] [y], end=" ")
            print()
        print("         1 2 3 ")
        print("        COLUMNAS")    
        print()
        print("La mesa 1, 2 y 3 tiene asientos para 2 peronas")
        print("La mesa 4, 5 y 6 tiene asientos para 4 personas")
        print("La mesa 7, 8 y 9 tiene asiento para 6 personas")
        print("\Pesione una tecla para continuar...") 
        msvcrt.getch()
         
          
def reservar_mesa():
    pass
def carta():
    pass
def pagar():
    pass
def cancelar():
    pass


while True:
   os.system('cls') 
   print("""\tMenú Restaurante\n
   1.Ver restaurante
   2.Reservar mesa
   3.Carta 
   4.Pagar
   5.Cancelar
   6.Salir\n""")
  
   opcion =  validar_opcion()

   if opcion ==1:
        ver_restaurante()
   elif opcion ==2:
        reservar_mesa()
   elif opcion ==3:
        carta() 
   elif opcion ==4:
        pagar()
   elif opcion ==5:
        cancelar()
   else: 
    print("Gracias, adios")
    break 