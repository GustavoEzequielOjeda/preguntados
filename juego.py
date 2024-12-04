from preguntas import preguntas_lista
from game_master import Juego
from submenu import configuracion_variables

#----------------------------  MUESTRA EL MENU PRUINCIPAL  ----------------
def mostrar_menu_principal():
        # ¿Que hace? Muestra las opcines que puede elegir el usuario
        # ¿Que recibe? ---
        # ¿Que devuelve? La opcion que elija el usuario
    print("\n---- MENÚ PRINCIPAL ----")
    print("1. Jugar")
    print("2. Configurar Juego")
    print("3. TOP")
    print("4. Agregar Preguntas")
    print("5. Estadisticas de las Preguntas")
    print("6. Salir")
    seleccion = input("Elige una opción: ")
    return seleccion
#----------------------------  EJECUTA EL MENU PRUINCIPAL  ----------------

def ejecutar():
        # ¿Que hace? Ejecuta el menu 
        # ¿Que recibe? La opcion que elija el usuario
        # ¿Que devuelve? Dependiendo de que opcion elija; Empieza el juego o Muestra un submenu
    puntos_sumar = 1  
    vida = 3  

    while True:
        seleccion = mostrar_menu_principal()

        if seleccion == '1':  
            print("\nIniciando el juego...")
            partida = Juego(vida, puntos_sumar, len(preguntas_lista))
            partida.validar_respuesta(preguntas_lista)
            print('Regresando al menú principal...\n')

        elif seleccion == '3':  
            print("\nMostrando el TOP de jugadores...")
            partida.ranking_lista()

        elif seleccion == '4':  
            print("\nMostrando Menu Agregar Preguntas...")
            # Agregar lógica del TOP aquí.
        
        elif seleccion == '5':  
            print("\nMostrando Estadisticas de Preguntas...")
            # Agregar lógica del TOP aquí.

        elif seleccion == '6':  
            print("\nSaliendo del juego. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, elige una opción del menú.")

ejecutar()