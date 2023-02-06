from mingus.core import chords
from mingus.containers import Note
from midiutil import MidiFile

class Chord:
    def __init__(self,notes):
        self.notes = notes
        self.midi = []

def get_chord_name(name):
    return chords.from_shorthand(name)

def note_num_conversion(note):
    note = int(Note(note, 4))
    return note

chord_names = ["Cmaj7","Fmaj","Gmaj"]
chord_dict = {}

for chord in chord_names:
    chord_dict[chord] = Chord(get_chord_name(chord))
    for note in chord_dict[chord].notes:
        chord_dict[chord].midi.append(note_num_conversion(note))
    print(chord_dict[chord].midi)

print(chord_dict)