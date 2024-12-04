def configuracion_variables(puntos_sumar:int, vida:int, tiempo_limite_preguntas:int):
    # ¿Que hace?    
    # ¿Que recibe?  
    # ¿Que devuelve?    
    while True:
        print(f"\n---- CONFIGURAR JUEGO ----")
        print(f"1. Cantidad de Puntos por Respuesta Correcta (Actual: {puntos_sumar})")
        print(f"2. Cantidad de Vidas (Actual: {vida})")
        print(f'3. Cantidad de Tiempo entre Preguntas (Actual: {tiempo_limite_preguntas})')
        print(f'4. Volver Atras')
        seleccion = input("Elige una opción: ")

        if seleccion == '1':
            print(' ')
            puntos_sumar = int(input('Ingrese cuántos puntos se ganan por pregunta respondida: '))
        elif seleccion == '2':
            print(' ')
            vida = int(input('Ingrese la cantidad de vidas que va a tener: '))
        elif seleccion == '3':
            print(' ')
            tiempo_limite_preguntas = int(input('Ingrese el tiempo entre preguntas (en segundos): '))
        elif seleccion == '4':
            print('Volviendo al Menú Principal...')
            break
        else:
            print("Opción inválida. Por favor, elige una opción del menú.")
    
    return puntos_sumar, vida, tiempo_limite_preguntas