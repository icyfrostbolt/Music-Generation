import tkinter as tk
from tkinter import *
import midi, parse_inst, notesfile

notes_data = []
inst = "Acoustic grand piano"
vol = 127
temp = 60
name_var = "Track"
note_numbers = notesfile.note_caller()

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
        octave_y = (10-self.octave)*140
        note_y = 0
        match self.note:
            case "C":
                note_y = 120
            case "D":
                note_y = 100
            case "E":
                note_y = 80
            case "F":
                note_y = 60
            case "G":
                note_y = 40
            case "A":
                note_y = 20
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

def update_settings():
    global inst, name, vol, temp
    volume = volumenameentry.get()
    instrument = instrumentnameentry.get()
    tempo = temponameentry.get()
    name = nameentry.get()
    try:
        volume_test = int(volume)
        tempo_test = int(tempo)
    except:
        return
    vol = int(volume)
    temp = int(tempo)
    if parse_inst.valid_inst():
        inst = instrument

def add_note():
    global notes_data
    note = notenameentry.get()
    octave = octavenameentry.get()
    start = timenameentry.get()
    length = durationnameentry.get()
    note_names = ["A","B","C","D","E","F","G","Ab","Bb","Db","Eb","Gb","G#","A#","C#","D#","F#"]
    chord_names = ["Amin","Amaj","Bmin","Bmaj","Cmin","Cmaj","Dmin","Dmaj",
    "Emin","Emaj","Fmin","Fmaj","Gmin","Gmaj","Abmin","Abmaj","Bbmin","Bbmaj",
    "Dbmin","Dbmaj","Ebmin","Ebmaj","Gbmin","Gbmaj"]
    if not note in note_names and not note in chord_names:
        return
    if note in note_names:
        notes_data.append(Note(note, int(octave), int(start), int(length)))
        notes_data[-1].set_y()
        notes_data[-1].init_button()
    else:
        for chord in note_numbers[f"{note}{octave}"].pitch:
            notes_data.append(Note(chord, int(octave), int(start), int(length)))
            notes_data[-1].set_y()
            notes_data[-1].init_button()
    try:
        octave_test = int(octave)
        start_test = int(start)
        length_test = int(length)
    except:
        return
    place()

def export_song():
    global inst, name_var, vol, temp, notes_data
    midi.export_song(inst, vol, temp, name_var, notes_data)

window = tk.Tk()
window.geometry("400x400")
window.title("Music Generator")

xcoord = 0
ycoord = -680

settings = tk.Button(text="Update Settings:", background="#03fc52", width="16",command=update_settings)
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

name = tk.Label(text="Name:")
nameentry = tk.Entry()
name.place(x=0,y=345)
nameentry.place(x=0,y=365)

notename = tk.Label(text="Note:")
notenameentry = tk.Entry()
notename.place(x=150,y=225)
notenameentry.place(x=150,y=245)

octavename = tk.Label(text="Octave:")
octavenameentry = tk.Entry()
octavename.place(x=150,y=265)
octavenameentry.place(x=150,y=285)

vertical_bar = tk.Label(width=2,height=13,bg="green")
vertical_bar.place(x=0,y=0)
octave_indicators = []
for octave in range(10):
    for note in range(7):
        match note:
            case 0:
                note_name = "B"
            case 1:
                note_name = "A"
            case 2:
                note_name = "G"
            case 3:
                note_name = "F"
            case 4:
                note_name = "E"
            case 5:
                note_name = "D"
            case 6:
                note_name = "C"
        octave_indicators.append([tk.Label(text=f"{note_name}{octave}",bg="green",width=2),0,(10-octave)*140+note*20])

timeindicator = []

timename = tk.Label(text="Time:")
timenameentry = tk.Entry()
timename.place(x=150,y=305)
timenameentry.place(x=150,y=325)

durationname = tk.Label(text="Duration:")
durationnameentry = tk.Entry()
durationname.place(x=150,y=345) 
durationnameentry.place(x=150,y=365)

button = tk.Button(text="Add note",width=16,height=0,bg="#03fc52",command=add_note)
button.place(x=150,y=200)

green_bar = tk.Label(width=60,height=1,bg="green")
green_bar.place(x=0,y=180)

exportbutton = tk.Button(text="Export",width=10,height=2,bg="#2bd639",command=export_song)
exportbutton.place(x=300,y=275)

# mouse wheel has a counter which coordinates to the synthesizer position

def place():
    global xcoord, ycoord, barnum
    for notes in notes_data:
        if notes.self_y+ycoord > 160:
            if notes.x+xcoord > 30:
                notes.button.place(x=notes.x+xcoord-10,y=notes.self_y+ycoord+300)
            else:
                notes.button.place(x=notes.x+xcoord+300,y=notes.self_y+ycoord+300)
        else:
            if notes.x+xcoord > 30:
                notes.button.place(x=notes.x+xcoord-10,y=notes.self_y+ycoord)
            else:
                notes.button.place(x=notes.x+xcoord-300,y=notes.self_y+ycoord)
    for item in octave_indicators:
        if item[2]+ycoord > 160:
            item[0].place(x=item[1],y=item[2]+ycoord+300)
        else:
            item[0].place(x=item[1],y=item[2]+ycoord)
    result = xcoord
    result = int(result)
    while len(timeindicator) < (result*-1)/10+10:
        timeindicator.append(tk.Label(text=f"{len(timeindicator)}",bg="green",width="5",anchor="w"))
    
    for time in timeindicator:
        time.place(x=(timeindicator.index(time)*40)+xcoord+30,y=180)

def mouse_wheel(event):
    global ycoord
    if event.delta == -120:
        if ycoord - 5 >= -1220:
            ycoord -= 5
    if event.delta == 120:
        if ycoord + 5 <= 0:
            ycoord += 5
    place()

def key_pressed(event):
    global xcoord, ycoord
    match event.keysym:
        case 'Left':
            xcoord -= 10
        case 'Right':
            if xcoord + 5 <= 0:
                xcoord += 10
        case 'Up':
            if ycoord + 5 <= 0:
                ycoord += 5
        case'Down':
            if ycoord - 5 >= -1220:
                ycoord -= 5
    place()

place()
window.bind("<Key>", key_pressed)
window.bind("<MouseWheel>", mouse_wheel)

window.mainloop()