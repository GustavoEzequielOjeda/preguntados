from preguntas import preguntas_lista
from game_master import Juego


#-----------------------------------------------ACA SE EJECUTA EL JUEGO-----------------------------------------------

def mostrar_menu_principal():
    print("\n---- MENÚ PRINCIPAL ----")
    print("1. Jugar")
    print("2. Configurar Juego")
    print("3. TOP")
    print("4. Agregar Preguntas")
    print("5. Estadísticas de las Preguntas")
    print("6. Salir")
    seleccion = input("Elige una opción: ")
    return seleccion
#-----------------------------------------MOSTAR MENU DE CONFIGURACION---------------------------------------

def mostrar_menu_configurar():
    print(f"\n---- CONFIGURAR JUEGO ----")
    print(f"1. Cantidad de Puntos por Respuesta Correcta")
    print(f"2. Cantidad de Vidas")
    print(f"3. Cantidad de Tiempo entre Preguntas")
    print(f"4. Volver al Menú Principal")
    print(' ')
    seleccion = input("Elige una opción: ")
    return seleccion


#-----------------------------------------------EJECUTA MENU-----------------------------------------------

def ejecutar():
    while True:
        seleccion = mostrar_menu_principal()
#----------INICIA EL JUEGO

        if seleccion == '1':  
            print("\nIniciando el juego...")
            partida = Juego(preguntas_lista)  
            partida.iniciar_partida()

#----------COFIGURACION DEL JUEGO

        elif seleccion == '2':  
            print("\nOpciones de configuración aún no implementadas.")

#----------MOSTRAR TOP

        elif seleccion == '3':  
            print("\nMostrando el TOP de jugadores...")

#---------AGREGAR PREGUNTA  
        elif seleccion == '4':  
            print("\nAgregando preguntas...")

#---------MOSTRAR ESTADISCAS

        elif seleccion == '5':  
            print("\nMostrando estadísticas de preguntas...")

#---------SALIENDO
        elif seleccion == '6':  
            print("\nSaliendo del juego. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción del menú.")

ejecutar()
