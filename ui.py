import tkinter as tk
from tkinter import *

notes_data = []
class Note():
    def __init__(self, note, octave, start, length):
        self.note = int(note)
        self.octave = int(octave)
        self.start = int(start)
        self.length = int(length)
        self.x = self.start*5
        self.y = None
        self.button = None
    
    def set_y(self):
        octave_y = self.octave*60
        note_y = 0
        match self.note:
            case "D":
                note_y = 10
            case "E":
                note_y = 20
            case "F":
                note_y = 30
            case "G":
                note_y = 40
            case "A":
                note_y = 50
            case "B":
                note_y = 60
        self.self_y = octave_y + note_y
    
    def init_button(self):
        self.button = tk.Label(height=2,background="red",width=self.length*5)

def add_note():
    global notes_data
    note = notenameentry.get()
    octave = octavenameentry.get()
    start = timenameentry.get()
    length = durationnameentry.get()
    notes_data.append(Note(note, octave, start, length))
    notes_data[-1].set_y()
    notes_data[-1].init_button()

window = tk.Tk()
window.geometry("400x400")
window.title("Music Generation")

xcoord = 0
ycoord = 0

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
durationname.place(x=200,y=345) 
durationnameentry.place(x=200,y=365)

button = tk.Button(text="Add note",width=25,height=0,bg="cyan",command=add_note)
button.place(x=200,y=200)

# mouse wheel has a counter which coordinates to the synthesizer position

def place():
    global xcoord, ycoord
    for notes in notes_data:
        notes.button.place(x=notes.x+xcoord,y=notes.self_y+ycoord)

def mouse_wheel(event):
    global ycoord
    if event.delta == -120:
        ycoord -= 1
    if event.delta == 120:
        ycoord += 1
    place()

def key_pressed(event):
    global xcoord
    if event.keysym == 'Left':
        xcoord -= 5
    if event.keysym == 'Right':
        xcoord += 5
    place()

place()
window.bind("<Key>", key_pressed)
window.bind("<MouseWheel>", mouse_wheel)

window.mainloop()