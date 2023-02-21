import mido

# Lesen Sie die MIDI-Datei ein
mid = mido.MidiFile("Hallelujah.mid")

# Überprüfen Sie die Informationen zur MIDI-Datei
print("Anzahl der Spuren:", len(mid.tracks))

# Durchlaufen Sie jede Note in jeder Spur
for i, track in enumerate(mid.tracks):
    print("Spur", i, "Anzahl der Noten:", len(track))
    for msg in track:
        print(msg)



# Definieren Sie die Mapping-Tabelle für 17 Tasten auf der Kalimba
kalimba_mapping = {
    60: 1,
    61: 2,
    62: 3,
    63: 4,
    64: 5,
    65: 6,
    66: 7,
    67: 8,
    68: 9,
    69: 10,
    70: 11,
    71: 12,
    72: 13,
    73: 14,
    74: 15,
    75: 16,
    76: 17
}

# Übertragen Sie die Noteninformationen auf eine Kalimba mit 17 Tasten
kalimba_track = mido.MidiTrack()
for msg in mid.tracks[0]:
    if msg.type == "note_on":
        note = msg.note
        if note in kalimba_mapping:
            new_note = kalimba_mapping[note]
            kalimba_track.append(
                mido.Message("note_on", note=new_note, velocity=msg.velocity, time=msg.time)
            )

# Hinzufügen der neuen Spur zur MIDI-Datei
kalimba_mid = mido.MidiFile()
kalimba_mid.tracks.append(kalimba_track)



# Überprüfen Sie, ob die Noten innerhalb des Bereichs von 17 Tasten liegen
# und passen Sie die Tonhöhen an
kalimba_track = mido.MidiTrack()
for msg in mid.tracks[0]:
    if msg.type == "note_on":
        note = msg.note
        if note in kalimba_mapping:
            new_note = kalimba_mapping[note]
            if new_note >= 1 and new_note <= 17:
                # Hier können Sie die Tonhöhen anpassen
                adjusted_note = new_note + 7
                kalimba_track.append(
                    mido.Message("note_on", note=adjusted_note, velocity=msg.velocity, time=msg.time)
                )

# Hinzufügen der neuen Spur zur MIDI-Datei
kalimba_mid = mido.MidiFile()
kalimba_mid.tracks.append(kalimba_track)

# Speichern Sie die MIDI-Datei
kalimba_mid.save("kalimba_arrangement.mid")