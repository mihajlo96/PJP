import numpy as np
import simpleaudio as sa
from tkinter import *

root = Tk()
root.title("Stimer")
root.geometry("309x330+400+175")
root.configure(background='#837e7e')



controller = 0

def stop():
    if controller == 1:
        play_obj.stop()

def open(fq):
    stop()
    global controller
    controller = 1
    frequency = fq
    fs = 44100
    seconds = 9

    t = np.linspace(0, seconds, seconds * fs, False)

    note = np.sin(frequency * t * 2 * np.pi)

    audio = note * (2 ** 15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)

    global play_obj
    play_obj = sa.play_buffer(audio, 1, 2, fs)

options = [
    "lista1",
    "lista2",
    "Wednesday",
    "Thursday",
    "Friday"
]

zvuk1 = 82.41
zvuk2 = 110
zvuk3 = 146.8
zvuk4 = 196
zvuk5 = 246.9
zvuk6 = 329.6
lista1 = [82.41, 110, 146.8, 196, 246.9, 329.6]
lista2 = [73.42, 110, 146.8, 196, 246.9, 329.6]

clicked = StringVar()
clicked.set(options[0])

def zvuk(opcija):
    global zvuk1
    global zvuk2
    global zvuk3
    global zvuk4
    global zvuk5
    global zvuk6

    if opcija == 'lista1':
        zvuk1 = lista1[0]
        zvuk2 = lista1[1]
        zvuk3 = lista1[2]
        zvuk4 = lista1[3]
        zvuk5 = lista1[4]
        zvuk6 = lista1[5]

    elif opcija == 'lista2':
        dugme1.configure(text="hello")
        zvuk1 = lista2[0]
        zvuk2 = lista2[1]
        zvuk3 = lista2[2]
        zvuk4 = lista2[3]
        zvuk5 = lista2[4]
        zvuk6 = lista2[5]

drop = OptionMenu(root, clicked, *options, command=zvuk)
drop.config(bg = "GREEN",fg= 'red')
drop.grid(row=0,column=3,padx=115)







dugme1 = Button(root, text="420HZ",padx = 20, command=lambda: open(zvuk1) )
dugme1.grid(row=1,column=3, pady = 20)

dugme2 = Button(root, text="420HZ",padx = 20, command=lambda: open(zvuk2) )
dugme2.grid(row=2,column=3)

dugme3 = Button(root, text="420HZ",padx = 20, command=lambda: open(zvuk3) )
dugme3.grid(row=3,column=3)

dugme4 = Button(root, text="420HZ",padx = 20, command=lambda: open(zvuk4) )
dugme4.grid(row=4,column=3)

dugme5 = Button(root, text="420HZ",padx = 20, command=lambda: open(zvuk5) )
dugme5.grid(row=5,column=3)

dugme6 = Button(root, text="420HZ",padx = 20, command=lambda: open(zvuk6) )
dugme6.grid(row=6,column=3)

btn_stop = Button(root, text="STOP", command=lambda: stop() )
btn_stop.grid(row=7,column=3,columnspan=2)

root.mainloop()