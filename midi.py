from mingus.containers import Note
from midiutil import MIDIFile
import notes, os, parse_inst

channel = 0 # only 1 channel in this project
time = 0  # beats
duration = 1 # beats
tempo = int(input("Tempo? (BPM): "))
volume = int(input("Volume? (0-127): "))
instrument = input("What MIDI Instrument? (Name): ")
max = 0 # helps determine maximum number of beats
longest_duration = 0 # longest duration of a beat

note_numbers = notes.note_caller()
inst_dict = parse_inst.get_instrument_codes()

def add_note_to_dict(note, time, duration):
    note.duration = duration
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

def open_song(name):
    notes = []
    song = open(name)
    song.readline()
    for data in song:
        notes.append(data.split(","))
    return notes

track_num = 0
directory = os.getcwd()
directory = os.path.join(directory, "CSV")
for item in sorted(os.listdir(directory)):
    track_num += 1

note_data = []
for number in range(track_num):
    note_time_dict = {}
    # add the notes to the song
    note_data.append(open_song(os.path.join(directory, f"song{number}.csv")))
    for item in note_data[-1]:
        add_note_to_dict(note_numbers[item[0]+item[1]], int(item[2]), int(item[3]))
    
    # row 1 = note
    # row 2 = octave
    # row 3 = start time
    # row 4 = duration

    MyMIDI = MIDIFile(track_num)
    MyMIDI.addTempo(number, time, tempo)
    MyMIDI.addProgramChange(number, channel, 0, inst_dict[instrument])

    while True:
        if max+longest_duration <= time:
            break
        if time in note_time_dict:
            for item in note_time_dict.get(time):
                for note_pitch in item.pitch:
                    MyMIDI.addNote(number, channel, note_pitch, time, item.duration, volume)
        time += 1

if os.path.exists(f"Track/Track.midi"):
    os.remove(f"Track/Track.midi")
with open(f"Track/Track.midi", "wb") as output_file:
    MyMIDI.writeFile(output_file)