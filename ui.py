import tkinter as tk
from tkinter import *

notes_data = []
class Note():
    def __init__(self, note, octave, start, length):
        self.note = note
        self.octave = int(octave)
        self.start = int(start)
        self.length = int(length)
        self.x = self.start*40
        self.y = None
        self.button = None
    
    def set_y(self):
        octave_y = self.octave*140
        note_y = 0
        match self.note:
            case "D":
                note_y = 20
            case "E":
                note_y = 40
            case "F":
                note_y = 60
            case "G":
                note_y = 80
            case "A":
                note_y = 100
            case "B":
                note_y = 120
        self.self_y = octave_y + note_y
    
    def color_choice(self):
        match self.note:
            case "C":
                return "red"
            case "D":
                return "orange"
            case "E":
                return "yellow"
            case "F":
                return "green"
            case "G":
                return "blue"
            case "A":
                return "purple"
            case "B":
                return "pink"

    def init_button(self):
        self.button = tk.Label(height=1,background=self.color_choice(),width=self.length*5)

def add_note():
    global notes_data
    note = notenameentry.get()
    note_names = ["A","B","C","D","E","F","G","Ab","Bb","Db","Eb","Gb","G#","A#","C#","D#","F#"]
    if not note in note_names:
        return
    octave = octavenameentry.get()
    start = timenameentry.get()
    length = durationnameentry.get()
    try:
        octave_test = int(octave)
        start_test = int(start)
        length_test = int(length)
    except:
        return
    notes_data.append(Note(note, octave, start, length))
    notes_data[-1].set_y()
    notes_data[-1].init_button()
    place()

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

octave_indicators = []
for octave in range(10):
    for note in range(7):
        match note:
            case 0:
                note_name = "C"
            case 1:
                note_name = "D"
            case 2:
                note_name = "E"
            case 3:
                note_name = "F"
            case 4:
                note_name = "G"
            case 5:
                note_name = "A"
            case 6:
                note_name = "B"
        octave_indicators.append([tk.Label(text=f"{note_name}{octave}",bg="orange",width=2),0,octave*140+note*20])

        

timename = tk.Label(text="Time:")
timenameentry = tk.Entry()
timename.place(x=200,y=305)
timenameentry.place(x=200,y=325)

durationname = tk.Label(text="Duration:")
durationnameentry = tk.Entry()
durationname.place(x=200,y=345) 
durationnameentry.place(x=200,y=365)

button = tk.Button(text="Add note",width=25,height=0,bg="cyan",command=add_note)
button.place(x=200,y=200)

# mouse wheel has a counter which coordinates to the synthesizer position

def place():
    global xcoord, ycoord
    for notes in notes_data:
        if notes.self_y+ycoord > 180:
            notes.button.place(x=notes.x+xcoord,y=notes.self_y+ycoord+300)
        else:
            notes.button.place(x=notes.x+xcoord,y=notes.self_y+ycoord)
    for item in octave_indicators:
        if item[2]+ycoord > 180:
            item[0].place(x=item[1],y=item[2]+ycoord+300)
        else:
            item[0].place(x=item[1],y=item[2]+ycoord)

def mouse_wheel(event):
    global ycoord
    if event.delta == -120:
        ycoord -= 5
    if event.delta == 120:
        ycoord += 5
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