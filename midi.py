from mingus.containers import Note
from midiutil import MIDIFile
import notesfile, os, parse_inst

class Chord:
    def __init__(self,note,octave,duration):
        self.note = note
        self.octave = octave
        self.pitch = []
        self.duration = duration

note_time_dict = {}

def add_note_to_dict(note, time, duration, octave):
    global longest_duration, max_beats
    max_beats = 0 # helps determine maximum number of beats
    if not time in note_time_dict:
        if max_beats <= time:
            max_beats = time
            longest_duration = duration
        note_time_dict[time] = [Chord(note,octave,duration)]
    else:
        note_time_dict[time].append(Chord(note,octave,duration))
        if duration >= longest_duration:
            longest_duration = duration
    return longest_duration
    
def export_song(instrument, volume, tempo, export_name, note_data):
    channel = 0
    time = 0  # beats
    longest_duration = 0 # longest duration of a beat

    note_numbers = notesfile.note_caller()
    inst_dict = parse_inst.get_instrument_codes()

    # add the notes to the song

    for notes in note_data:
        temp_long = add_note_to_dict(notes.note, notes.start, notes.length, notes.octave)
        if temp_long > longest_duration:
            longest_duration = temp_long

    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(0, time, tempo)
    MyMIDI.addProgramChange(0, channel, 0, inst_dict[instrument])

    while True:
        if max_beats+longest_duration <= time:
            break
        if time in note_time_dict:
            for item in note_time_dict.get(time):
                MyMIDI.addNote(0, channel, notesfile.note_num_conversion(item.note, item.octave), time, item.duration, volume)
        time += 1

    if os.path.exists(f"Track/{export_name}.midi"):
        os.remove(f"Track/{export_name}.midi")
    with open(f"Track/{export_name}.midi", "wb") as output_file:
        MyMIDI.writeFile(output_file)