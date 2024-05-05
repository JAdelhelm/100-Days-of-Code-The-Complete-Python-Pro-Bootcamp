from queue import Queue
from functools import partial
from turtle import Screen, Turtle
from threading import Thread, active_count

STEPS = 3
LENGTH = 300

def koch_curve(turtle, steps, length):
    if steps == 0:
        actions.put((turtle.forward, length))
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, steps - 1, length / 3)
            actions.put((turtle.left, angle))

def process_queue():
    while not actions.empty():
        action, *arguments = actions.get()
        action(*arguments)

    if active_count() > 1:
        screen.ontimer(process_queue, 1)

screen = Screen()
actions = Queue(1)  # size = number of hardware threads you have - 1

turtle1 = Turtle('turtle')
turtle1.hideturtle()
turtle1.speed('fastest')
turtle1.color('red')
turtle1.penup()
turtle1.right(30)
turtle1.backward(3**0.5 * LENGTH / 3)
turtle1.left(30)
turtle1.pendown()

turtle2 = turtle1.clone()
turtle2.color('green')
turtle2.penup()
turtle2.forward(LENGTH)
turtle2.right(120)
turtle2.pendown()

turtle3 = turtle1.clone()
turtle3.speed('fastest')
turtle3.color('blue')
turtle3.penup()
turtle3.right(240)
turtle3.backward(LENGTH)
turtle3.pendown()

thread1 = Thread(target=partial(koch_curve, turtle1, STEPS, LENGTH))
thread1.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread1.start()

thread2 = Thread(target=partial(koch_curve, turtle2, STEPS, LENGTH))
thread2.daemon = True
thread2.start()

thread3 = Thread(target=partial(koch_curve, turtle3, STEPS, LENGTH))
thread3.daemon = True
thread3.start()

process_queue()

screen.exitonclick()