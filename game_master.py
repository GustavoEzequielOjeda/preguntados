from preguntas import preguntas_lista
import random
import json

ranking_global = []

class Juego:

    def __init__(self, vida:int, puntos_sumar:int, preguntas_cantidad:int):
        # ¿Que hace? Metodo Contructor
        # ¿Que recibe? Cant de Vida, Bandera, 
        # ¿Que devuelve? ...
        self.vida = vida
        self.puntos_sumar = puntos_sumar
        self.preguntas_cantidad = preguntas_cantidad    
        self.bandera = True
        self.puntos = 0
        self.respuestas_correctas = 0
        self.ranking = []
#-----------------------------INICIA EL JUEGO-------------------------
    def validar_respuesta(self, preguntas:list):
        # ¿Que hace? Inicia el juego y valida si la respuesta es correcta
        # ¿Que recibe? Una lista con todas las preguntas
        # ¿Que devuelve? ...
        random.shuffle(preguntas)
        while self.bandera:
                            
            for pregunta in preguntas:
                if self.vida == 0 or self.preguntas_cantidad == 0:
                    self.partida_terminar()
                    return     

                print(pregunta["pregunta"])
                for respuestas_posibles in pregunta["respuestas"]:
                    print(respuestas_posibles)
                respuesta_usuario = str(input("Ingrese su respuesta (A, B, C, D): ")).upper()
                while respuesta_usuario != "A" and respuesta_usuario != "B" and respuesta_usuario != "C" and respuesta_usuario != "D":
                    print(' ')
                    print("Respuesta invalida. Por favor ingrese A, B, C o D")
                    print(' ')
                    respuesta_usuario = str(input("Ingrese su respuesta (A, B, C, D): ")).upper()
                if respuesta_usuario == pregunta["respuesta_correcta"]:
                    print(' ')
                    print("Felicidades, la respuesta es correcta!")
                    print(' ')
                    self.preguntas_cantidad -= 1
                    self.puntos += self.puntos_sumar
                    self.respuestas_correctas += 1
                else:
                    print(' ')
                    print("La respuesta es incorrecta :(")
                    print(' ')
                    self.preguntas_cantidad -= 1
                    self.vida -= 1     
 
    def partida_terminar(self) -> list:
        # ¿Que hace? Termina la partida
        # ¿Que recibe? La vida y la cantidad de preguntas
        # ¿Que devuelve? bandera = False
        if not self.bandera:
            return

        self.bandera = False
        if self.vida == 0:
            print(' ')
            print('¡YOU DIE!')
        elif self.preguntas_cantidad == 0:
            print(' ')
            print('Ya no hay mas preguntas!')
            print('Felicidades!!!')

        print(f'Puntaje : {self.puntos}')
        print(f'Vida: {self.vida}')
        nombre_usuario = input("Ingrese el nombre de usuario: ")

        ranking_global.append((nombre_usuario, self.puntos))
        ranking_global.sort(key=lambda x: x[1], reverse=True)

        # ¿Que hace? Ejecuta el menu 
        # ¿Que recibe? Una lista
        # ¿Que devuelve? Un print
    def ranking_lista(self):
        top_10 = ranking_global[:10]
        print("\n--- Top 10 jugadores ---")
        for i, (nombre, puntos) in enumerate(top_10, 1):
            print(f"{i}. {nombre} - {puntos} puntos")