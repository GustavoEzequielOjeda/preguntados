from preguntas import preguntas_lista
import random
import json
archivo_ranking = "ranking.json"

class Juego:

    def __init__(self, vida:int, puntos_sumar:int, preguntas_cantidad:int):
        # ¿Que hace? Metodo Contructor
        # ¿Que recibe? Cant de Vida, Bandera, 
        # ¿Que devuelve? ...
        self.vida = vida
        self.puntos_sumar = puntos_sumar
        self.preguntas_cantidad = preguntas_cantidad    


    bandera = True
    puntos = 0
    respuestas_correctas = 0

    


#-----------------------------INICIA EL JUEGO-------------------------
    def validar_respuesta(self, preguntas:list):
        # ¿Que hace? Inicia el juego y valida si la respuesta es correcta
        # ¿Que recibe? Una lista con todas las preguntas
        # ¿Que devuelve? ...
        random.shuffle(preguntas)
        while self.bandera == True:

            if self.vida == 0 or self.preguntas_cantidad == 0:
                self.partida_terminar()
                
                        
            for pregunta in preguntas:
                print(pregunta["pregunta"])
                for respuestas_posibles in pregunta["respuestas"]:
                    print(respuestas_posibles)
                respuesta_usuario = str(input("Ingrese su respuesta (A, B, C, D): ")).upper()
                while respuesta_usuario != "A" and respuesta_usuario != "B" and respuesta_usuario != "C" and respuesta_usuario != "D":
                    print("Respuesta invalida. Por favor ingrese A, B, C o D")
                    respuesta_usuario = str(input("Ingrese su respuesta (A, B, C, D): ")).upper()
                if respuesta_usuario == pregunta["respuesta_correcta"]:
                    print("Felicidades, la respuesta es correcta!")
                    self.preguntas_cantidad -= 1
                    self.puntos += self.puntos_sumar
                    self.respuestas_correctas += 1
                else:
                    print("La respuesta es incorrecta :(")
                    self.preguntas_cantidad -= 1
                    self.vida -= 1     
 
    def partida_terminar(self):
        # ¿Que hace? Termina la partida
        # ¿Que recibe? La vida y la cantidad de preguntas
        # ¿Que devuelve? bandera = False
        if self.vida == 0:
            print('¡YOU DIE!')
            self.bandera = False
            nombre_usuario = input("Ingrese el nombre de usuario: ")
        elif self.preguntas_cantidad == 0:
            print('Ya no hay mas preguntas!')
            self.bandera = False
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            print(f"Puntaje : {self.puntos} Vida: {self.vida}")

        jugador = []
        jugador.append(nombre_usuario, self.puntos, self.respuestas_correctas)
                        
        return jugador 



#----------------------------RANKING 10--------------------------------
'''    
    def ranking(lista):
    lista.sort(key=lambda x: x[1], reverse=True)
    ranking = lista[:10]

    for i, (nombre, puntos) in enumerate(ranking, 1):
        print(f"{i}. {nombre} - {puntos} puntos")

'''