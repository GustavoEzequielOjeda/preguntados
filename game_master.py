from preguntas import preguntas_lista
from submenu import configuracion_variables

import time
import random

archivo_ranking = "ranking.json"

ranking_global = []
import time
import random

class Juego:

    def _init_(self, vida:int, puntos_sumar:int, preguntas_cantidad:int, tiempo_limite_pregunta:int):
    # ¿Que hace? 
    # ¿Que recibe? 
    # ¿Que devuelve? 
        self.vida = vida
        self.puntos_sumar = puntos_sumar
        self.preguntas_cantidad = preguntas_cantidad
        self.bandera = True
        self.puntos = 0
        self.respuestas_correctas = 0
        self.tiempo_inicio_juego = time.time()  # Para el cronómetro total del juego
        self.tiempo_limite_pregunta = tiempo_limite_pregunta  # 10 segundos para cada pregunta

    def validar_respuesta(self, preguntas:list):
        # ¿Que hace? Valida si la Reespuesta es Correcta o no (tambien el tiempo) 
        # ¿Que recibe? La Lista de Preguntas
        # ¿Que devuelve? ---
        
        random.shuffle(preguntas)  # Barajar las preguntas una vez al inicio
        pregunta_index = 0  # Índice para llevar control de las preguntas
        while self.bandera:
            if self.vida == 0 or pregunta_index >= len(preguntas):  # Verificar si se acabaron las preguntas o las vidas
                self.partida_terminar()
                return

            pregunta = preguntas[pregunta_index]  # Tomar la siguiente pregunta
            print(pregunta["pregunta"])
            for respuestas_posibles in pregunta["respuestas"]:
                print(respuestas_posibles)

            #-------    INICIA EL TIEMPO  ------------
            tiempo_inicio = time.time()
            respuesta_usuario = None

            while time.time() - tiempo_inicio < self.tiempo_limite_pregunta:
                if respuesta_usuario in ["A", "B", "C", "D"]:
                    break
                elif respuesta_usuario is None:  # Si no se ha dado respuesta aún
                    respuesta_usuario = str(input(f"Tiempo restante: {int(self.tiempo_limite_pregunta - (time.time() - tiempo_inicio))} segundos. Ingrese su respuesta (A, B, C, D): ")).upper()
                else:
                    print("Respuesta inválida. Por favor ingrese A, B, C o D")
                    respuesta_usuario = str(input("Ingrese su respuesta (A, B, C, D): ")).upper()

            #-------    (-)VIDA SI PIERDE TIEMPO  ------------
            if time.time() - tiempo_inicio >= self.tiempo_limite_pregunta:
                print("Tiempo expirado. Has perdido una vida.")
                self.vida -= 1
                pregunta_index += 1  # Pasar a la siguiente pregunta
                continue  # Salta a la siguiente pregunta

            #-------    COMPARA LA RTA DEL USUARIO CON LA CORRECTA ------------
            if respuesta_usuario == pregunta["respuesta_correcta"]:
                print("Felicidades, la respuesta es correcta!")
                self.puntos += self.puntos_sumar
                self.respuestas_correctas += 1
            else:
                print("La respuesta es incorrecta :(")
                self.vida -= 1

            pregunta_index += 1  
        #-------    DEFINE SI TERMINA LA PARTIDA ------------
    def partida_terminar(self):
    # ¿Que hace? 
    # ¿Que recibe? 
    # ¿Que devuelve? 
        tiempo_total = time.time() - self.tiempo_inicio_juego
        minutos, segundos = divmod(int(tiempo_total), 60)

        self.bandera = False
        if self.vida == 0:
            print('¡YOU DIE!')
        elif self.preguntas_cantidad == 0:
            print('Ya no hay más preguntas!')
            print('Felicidades!!!')

        print(f'Puntaje : {self.puntos}')
        print(f'Vida: {self.vida}')
        print(f'Tiempo total jugado: {minutos} minutos {segundos} segundos')
        nombre_usuario = input("Ingrese el nombre de usuario: ")

        ranking_global.append((nombre_usuario, self.puntos))
        ranking_global.sort(key=lambda x: x[1], reverse=True)

        jugador = [nombre_usuario, self.puntos, self.respuestas_correctas, f'{minutos}m {segundos}s']
        return jugador

#----------------------------RANKING 10-------------------------------- 

    def ranking_lista(self):
    # ¿Que hace? Limita la lista de tuplas a 10 para luego recorrerlo 
    # ¿Que recibe? Recibe una lista
    # ¿Que devuelve? Un print del top 10
        top_10 = ranking_global[:10]
        print("\n--- Top 10 jugadores ---")
        for i, (nombre, puntos) in enumerate(top_10, 1):
            print(f"{i}. {nombre} - {puntos} puntos")