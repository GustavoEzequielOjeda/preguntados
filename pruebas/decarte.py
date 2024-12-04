#DECARTE DE game_master.py------
'''
import random

class Juego:

    def __init__(self, preguntas, vidas=3):
        self.preguntas = preguntas  # ! Llama a la lista de preguntas.
        self.pregunta_actual = ''  # ! La pregunta actual
        self.preguntas_usadas = []  # ! Almacena preguntas ya utilizadas
        self.respuesta_correcta = ''  # ! Respuesta correcta de la pregunta actual
        self.jugador_nombre = ''  # ! Nombre del jugador
        self.jugador_puntuacion = 0  # ! Puntuación del jugador
        self.vidas = vidas  # ! Vidas del jugador
        self.corriendo = True  # ! Estado del juego

#---------------INICIA LA PARTIDA   
    def iniciar_partida(self):
        print("\n¡Bienvenido al juego de Preguntados!")
        self.jugador_nombre = input("Por favor, ingresa tu nombre: ") 
        while self.vidas > 0 and self.corriendo: 
            self.pregunta_obtener()
            self.validar_preguntas()
        print("\nFin del juego.")
        print(f"Jugador: {self.jugador_nombre}")
        print(f"Puntuación: {self.jugador_puntuacion}")
        print("Gracias por jugar.")

#---------------BUSCA UNA PREGUNTA EN LA LISTA   
    def pregunta_obtener(self):
        if self.pregunta_actual :
            print("¡No hay más preguntas disponibles!")
            self.corriendo = False
            return

        self.pregunta_actual = random.choice(self.preguntas)
        self.respuesta_correcta = self.pregunta_actual['respuesta_correcta']
        print("\n" + self.pregunta_actual['pregunta'])
        for respuesta in self.pregunta_actual['respuestas']:
            print(respuesta)
        self.preguntas_usadas.append(self.pregunta_actual)  

#---------------VALIDA SI LA PREGUTNA ES CORRECTA
    def validar_preguntas(self):
        respuesta_usuario = input('\nIngrese la respuesta correcta (A, B, C, D): ').strip().upper()
        while respuesta_usuario not in ['A', 'B', 'C', 'D']:
            print('La respuesta no es válida. Por favor, ingresa A, B, C o D.')
            respuesta_usuario = input('Ingrese la respuesta correcta (A, B, C, D): ').strip().upper()

        if respuesta_usuario == self.respuesta_correcta:
            print('¡Correcto!')
            self.jugador_puntuacion += 1
        else:
            print(f'Incorrecto!')
            print('')
            print(f'La respuesta correcta era: {self.respuesta_correcta}')
            self.vidas -= 1
            print(f'Te quedan {self.vidas} vidas.')
'''