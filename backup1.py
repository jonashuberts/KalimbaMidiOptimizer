import mido
from mido import MidiFile, MidiTrack, Message
import os
import tkinter as tk
from tkinter import filedialog

# Funktion zum Entfernen von Noten
def remove_notes(midi_file):
    # Laden der midi-Datei
    mid = MidiFile(midi_file)

    # Durchlaufen jeder Spur in der midi-Datei
    for i, track in enumerate(mid.tracks):
        # Speichern der Noten in einer Liste
        notes = []
        for msg in track:
            # Überprüfen, ob die Nachricht eine Note-On-Nachricht ist
            if msg.type == 'note_on':
                # Überprüfen, ob die Note innerhalb des angegebenen Bereichs liegt
                if msg.note >= 60 and msg.note <= 84:
                    notes.append(msg)
        # Überschreiben der Spur mit den entfernten Noten
        mid.tracks[i] = MidiTrack(notes)

    # Speichern der modifizierten midi-Datei
    filename, file_extension = os.path.splitext(midi_file)
    mid.save(filename + '_Kalimba' + file_extension)

# Dialogfenster zur Auswahl der midi-Datei
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("MIDI Files", "*.mid")])

# Aufruf der Funktion mit der ausgewählten midi-Datei
remove_notes(file_path)