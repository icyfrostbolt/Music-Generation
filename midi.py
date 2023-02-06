from mingus.containers import Note
from midiutil import MIDIFile

track = 0
channel = 0
time = 0  # beats
duration = 1  # beats
tempo = 120
volume = 100

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(array_of_note_numbers): # create nested list
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("file", "wb") as output_file:
    MyMIDI.writeFile(output_file)