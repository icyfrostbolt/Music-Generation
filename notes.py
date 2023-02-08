from mingus.core import chords
from mingus.containers import Note
import mingus.core.notes as notes

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
    chord_dict = {}
    chord_names = ["Amin","Amaj","Bmin","Bmaj","Cmin","Cmaj","Dmin","Dmaj",
    "Emin","Emaj","Fmin","Fmaj","Gmin","Gmaj","Abmin","Abmaj","Bbmin","Bbmaj",
    "Dbmin","Dbmaj","Ebmin","Ebmaj","Gbmin","Gbmaj"]

    note_names = ["A","B","C","D","E","F","G","Ab","Bb","Db","Eb","Gb"]
    note_dict = single_notes(note_names)
    chord_dict.update(note_dict)

    for chord in chord_names:
        chord_dict[chord] = Chord(get_chord_name(chord))
        for note in chord_dict[chord].notes:
            chord_dict[chord].pitch.append(note_num_conversion(note))
    return chord_dict

def single_notes(note_names):
    note_pitch = {}
    for note_name in note_names:
        note_pitch[note_name] = Chord(note_name)
        note_pitch[note_name].pitch.append(notes.note_to_int(note_name))
    return note_pitch
