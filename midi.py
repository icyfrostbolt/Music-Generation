from mingus.containers import Note
from midiutil import MIDIFile
import notes, os, parse_inst

channel = 0
time = 0  # beats
duration = 4  # beats
tempo = 120
volume = 100
max = 0
longest_duration = 0

note_numbers = notes.note_caller()
note_time_dict = {}
inst_dict = parse_inst.get_instrument_codes()

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
    # add the notes to the song
    note_data.append(open_song(f"CSV/song{number}.csv"))
    for item in note_data[-1]:
        add_note_to_dict(note_numbers[item[0]+item[1]],int(item[2]),int(item[3]))
    
    # row 1 = note
    # row 2 = octave
    # row 3 = start time
    # row 4 = duration

    MyMIDI = MIDIFile(track_num)
    MyMIDI.addTempo(number, time, tempo)
    MyMIDI.addProgramChange(number, channel, 0, inst_dict["Bird tweet"])

    while True:
        if max+longest_duration <= time:
            break
        if time in note_time_dict:
            for item in note_time_dict.get(time):
                for note_pitch in item.pitch:
                    MyMIDI.addNote(number, channel, note_pitch, time, duration, volume)
        time += 1

    if os.path.exists(f"Track{number}.midi"):
        os.remove(f"Track{number}.midi")
    with open(f"Track/Track{number}.midi", "wb") as output_file:
        MyMIDI.writeFile(output_file)