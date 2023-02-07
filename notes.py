from mingus.core import chords
from mingus.containers import Note

class Chord:
    def __init__(self,notes):
        self.notes = notes
        self.pitch = []

def get_chord_name(name):
    return chords.from_shorthand(name)

def note_num_conversion(note):
    note = int(Note(note, 4))
    return note

def note_caller():
    chord_names = ["Cmaj7","Fmaj","Gmaj","Amin7"]
    chord_dict = {}

    for chord in chord_names:
        chord_dict[chord] = Chord(get_chord_name(chord))
        for note in chord_dict[chord].notes:
            chord_dict[chord].pitch.append(note_num_conversion(note))
    return chord_dict