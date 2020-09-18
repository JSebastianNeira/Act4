# Juan Sebastián Neira González a01570411
# Adán Daniel Márquez Hernández a00827172
from random import randrange #importa una función que elige numeros random dentro de un rango
from turtle import * #importa los elementos de la libreria de turtle
from freegames import vector #importa el juego

ball = vector(-200, -200) #Guarda la posición de la pelota
speed = vector(0, 0) #Guarda la velocidad de la pelota
targets = [] #Guarda los targets

def tap(x, y): #Función que hace el movimiento de la bola segun los taps en la pantalla
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy): #Verifica que las posiciones no esten fuera de la pantalla, entre -200 y 200
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw(): #Dibuja la pelota y los targets
    "Draw ball and targets."
    clear()

    for target in targets: #Por cada elemento de la lista, va dibujando un punto azul, los targets 
        goto(target.x, target.y)
        dot(20, 'orange')

    if inside(ball): #Verifica que las posiciones esten adentro de la pantalla y dibuja un punto rojo, proyectil
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move(): #Mueve los targets y la pelota
    "Move ball and targets."
    if randrange(40) == 0: #Genera un numero aleatorio con tope en el cuarenta y verifica si es igual a 0
        y = randrange(-150, 150) #Genera un numero random que determina la posicion en Y en la que salen las pelotas
        target = vector(200, y) #Hace que todas las pelotas empiecen del lado derecho, con target.x = 200
        targets.append(target) #Agrega el nuevo target a la lista de targets

    for target in targets: #Hace que se muevan las pelotas hacia la izquierda, esta es la velocidad en x de los targets
        target.x -= 5

    if inside(ball): #Verifica que las posiciones esten adentro de la pantalla y modifica la velocidad en y de la pelota
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy() #Genera una copia de la lista targets
    targets.clear() #Borra los elementos de la lista origianl

    for target in dupe: #Verifica que la pelota y el target hayan chocado
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets: #Verifica que los targets esten adentro de la pantalla
        if not inside(target):
            target.x = 200
            '''
            #Si los targets salen de la pantalla, se cambia la coordenada en x a 200, para que salgan 
            de nuevo del lado derecho, teniendo así un juego infinito
            '''

    ontimer(move, 10) #Determina el tiempo con el que sea realiza, en mili segundos 

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap) #Función que lee el clic, para disparar el proyectil
move() #Función que inicia el juego
done()