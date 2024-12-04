def configuracion_variables(puntos_sumar:int, vida:int):
    while True:
        print(f"\n---- CONFIGURAR JUEGO ----")
        print(f"1. Cantidad de Puntos por Respuesta Correcta (Actual: {puntos_sumar})")
        print(f"2. Cantidad de Vidas (Actual: {vida})")
        print(f"3. Volver al Menú Principal")
        seleccion = input("Elige una opción: ")

        if seleccion == '1':
            print(' ')
            puntos_sumar = int(input('Ingrese cuántos puntos se ganan por pregunta respondida: '))
        elif seleccion == '2':
            print(' ')
            vida = int(input('Ingrese la cantidad de vidas que va a tener: '))
        elif seleccion == '3':
            print('Volviendo al Menú Principal...')
            break
        else:
            print("Opción inválida. Por favor, elige una opción del menú.")
    
    return puntos_sumar, vida

