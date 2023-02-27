import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("400x400")
window.title("Music Generation")

def key_pressed(event):
    global xcoord
    if event.char == 'Left':
        xcoord += 1
    if event.char == 'Right':
        xcoord -= 1

window.bind("<Key>", key_pressed)

button = tk.Button(text="Add note",width=25,height=0,bg="cyan")
button.place(x=200,y=200)

settings = tk.Label(text="General Settings:", background="cyan", width="25")
settings.place(x=0,y=200)

volumename = tk.Label(text="Volume:")
volumenameentry = tk.Entry()
volumename.place(x=0,y=225)
volumenameentry.place(x=0,y=245)

instrumentname = tk.Label(text="Instrument:")
instrumentnameentry = tk.Entry()
instrumentname.place(x=0,y=265)
instrumentnameentry.place(x=0,y=285)

temponame = tk.Label(text="Tempo:")
temponameentry = tk.Entry()
temponame.place(x=0,y=305)
temponameentry.place(x=0,y=325)

settings = tk.Label(text="Track Settings", background="cyan", width="25")
settings.place(x=0,y=345)

track_buttons = []
xcoord = 0
for i in range(7):
   buttontemp = tk.Button(text=str(i+1), width=2, height=0, bg="white")
   track_buttons.append(buttontemp)

for num in range(len(track_buttons)):
    track_buttons[num].place(x=25*(num),y=365)

notename = tk.Label(text="Note:")
notenameentry = tk.Entry()
notename.place(x=200,y=225)
notenameentry.place(x=200,y=245)

octavename = tk.Label(text="Octave:")
octavenameentry = tk.Entry()
octavename.place(x=200,y=265)
octavenameentry.place(x=200,y=285)

timename = tk.Label(text="Time:")
timenameentry = tk.Entry()
timename.place(x=200,y=305)
timenameentry.place(x=200,y=325)

durationname = tk.Label(text="Duration Name:")
durationnameentry = tk.Entry()
durationname.place(x=200+xcoord,y=345) 
durationnameentry.place(x=200+xcoord,y=365)

# mouse wheel has a counter which coordinates to the synthesizer position

def mouse_wheel(event):
    global count
    if event.delta == -120:
        count -= 1 # scroll down
    if event.delta == 120:
        count += 1 # scroll up
    label['text'] = count

count = 0
window.bind("<MouseWheel>", mouse_wheel)
label = tk.Label(window, font=('courier', 18, 'bold'), width=10)
label.pack(padx=40, pady=40)

window.mainloop()