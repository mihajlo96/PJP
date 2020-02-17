import numpy as np
import simpleaudio as sa
from tkinter import *

root = Tk()
root.title("Stimer")
root.geometry("359x370+400+175")
root.configure(background='grey')



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
    "Standard",
    "DropD",
    "HalfStepDown",
    "OpenG"
]

zvuk1 = 82.41
zvuk2 = 110
zvuk3 = 146.8
zvuk4 = 196
zvuk5 = 246.9
zvuk6 = 329.6
Standard = [82.41, 110, 146.83, 196, 246.94, 329.63]
DropD = [73.42, 110, 146.83, 196, 246.94, 329.63]
HalfStepDown = [77.78, 103.83, 138.59, 185, 233.08, 311.13]
OpenG = [73.42, 98, 146.83, 196, 246.94, 293.66]

clicked = StringVar()
clicked.set(options[0])

def zvuk(opcija):
    global zvuk1
    global zvuk2
    global zvuk3
    global zvuk4
    global zvuk5
    global zvuk6

    if opcija == 'Standard':
        dugme1.configure(text="E")
        dugme2.configure(text="A")
        dugme3.configure(text="D")
        dugme4.configure(text="G")
        dugme5.configure(text="H")
        dugme6.configure(text="E")
        zvuk1 = Standard[0]
        zvuk2 = Standard[1]
        zvuk3 = Standard[2]
        zvuk4 = Standard[3]
        zvuk5 = Standard[4]
        zvuk6 = Standard[5]

    elif opcija == 'DropD':
        dugme1.configure(text="D")
        dugme2.configure(text="A")
        dugme3.configure(text="D")
        dugme4.configure(text="G")
        dugme5.configure(text="H")
        dugme6.configure(text="E")
        zvuk1 = DropD[0]
        zvuk2 = DropD[1]
        zvuk3 = DropD[2]
        zvuk4 = DropD[3]
        zvuk5 = DropD[4]
        zvuk6 = DropD[5]

    elif opcija == 'HalfStepDown':
        dugme1.configure(text="D#", padx = 29)
        dugme2.configure(text="G#")
        dugme3.configure(text="C#")
        dugme4.configure(text="F#")
        dugme5.configure(text="A#")
        dugme6.configure(text="D#", padx = 29)
        zvuk1 = HalfStepDown[0]
        zvuk2 = HalfStepDown[1]
        zvuk3 = HalfStepDown[2]
        zvuk4 = HalfStepDown[3]
        zvuk5 = HalfStepDown[4]
        zvuk6 = HalfStepDown[5]
    elif opcija == 'OpenG':
        dugme1.configure(text="D", )
        dugme2.configure(text="G")
        dugme3.configure(text="D")
        dugme4.configure(text="G")
        dugme5.configure(text="H")
        dugme6.configure(text="D")
        zvuk1 = OpenG[0]
        zvuk2 = OpenG[1]
        zvuk3 = OpenG[2]
        zvuk4 = OpenG[3]
        zvuk5 = OpenG[4]
        zvuk6 = OpenG[5]

drop = OptionMenu(root, clicked, *options, command=zvuk)
drop.config(width=13)
drop.grid(row=0,column=3,padx=115, pady = 10)







dugme1 = Button(root, text="E",padx = 30, pady = 10, command=lambda: open(zvuk1) )
dugme1.grid(row=1,column=3)

dugme2 = Button(root, text="A",padx = 29, pady = 10, command=lambda: open(zvuk2) )
dugme2.grid(row=2,column=3)

dugme3 = Button(root, text="D",padx = 29, pady = 10, command=lambda: open(zvuk3) )
dugme3.grid(row=3,column=3)

dugme4 = Button(root, text="G",padx = 29, pady = 10, command=lambda: open(zvuk4) )
dugme4.grid(row=4,column=3)

dugme5 = Button(root, text="H",padx = 28, pady = 10, command=lambda: open(zvuk5) )
dugme5.grid(row=5,column=3)

dugme6 = Button(root, text="E",padx = 30, pady = 10, command=lambda: open(zvuk6) )
dugme6.grid(row=6,column=3)

btn_stop = Button(root, text="STOP", padx = 10, command=lambda: stop() )
btn_stop.grid(row=7,column=3,columnspan=2)

root.mainloop()