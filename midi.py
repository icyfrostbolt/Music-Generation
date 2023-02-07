from mingus.containers import Note
from midiutil import MIDIFile
import notes, os

track = 0
channel = 0
time = 0  # beats
duration = 4  # beats
tempo = 120
volume = 100
max = 0
longest_duration = 0

note_numbers = notes.note_caller()
note_time_dict = {}

def add_note_to_dict(note, time, duration):
    global max, longest_duration
    if not time in note_time_dict:
        if max <= time:
            max = time
            longest_duration = duration
        note_time_dict[time] = [note]
    else:
        note_time_dict[time].append(note)
        if duration >= longest_duration:
            longest_duration = duration

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

while True:
    if max+longest_duration <= time:
        break
    if time in note_time_dict:
        for item in note_time_dict.get(time):
            for note_pitch in item.pitch:
                MyMIDI.addNote(track, channel, note_pitch, time, duration, volume)
    time += 1

if os.path.exists("Track.midi"):
  os.remove("Track.midi")
with open("Track.midi", "wb") as output_file:
    MyMIDI.writeFile(output_file)