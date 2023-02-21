#Todo: Add a file upload button

import mido
from mido import MidiFile, MidiTrack, Message
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Funktion zum Entfernen von Noten
def remove_notes(midi_file, num_keys):
    # Liste mit den Notenbereichen für verschiedene Anzahl von Tasten
    key_ranges = {
        8: (60, 67),
        17: (60, 84),
        21: (60, 96)
    }

    # Bereich der erlaubten Noten aus der Liste auswählen
    key_range = key_ranges.get(num_keys, (60, 96))

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
                if msg.note >= key_range[0] and msg.note <= key_range[1]:
                    notes.append(msg)
        # Überschreiben der Spur mit den entfernten Noten
        mid.tracks[i] = MidiTrack(notes)

    # Speichern der modifizierten midi-Datei
    filename, file_extension = os.path.splitext(midi_file)
    mid.save(filename + '_Kalimba' + file_extension)

# Funktion zur Anzeige eines Dialogfensters zur Auswahl der midi-Datei
def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("MIDI Files", "*.mid")])
    if file_path:
        # Auslesen der ausgewählten Anzahl von Tasten
        num_keys = int(keys_var.get())
        # Aufruf der Funktion mit der ausgewählten midi-Datei und der Anzahl von Tasten
        remove_notes(file_path, num_keys)
        messagebox.showinfo("Information", "Datei wurde konvertiert.")
    else:
        messagebox.showerror("Error", "Es wurde keine Datei ausgewählt.")

# Hauptfenster der Anwendung
root = tk.Tk()
root.title("Kalimba Midi Generator")

# Variablen zur Speicherung der Auswahl des Benutzers
keys_var = tk.StringVar(value='17')

# Radio Buttons zur Auswahl der Anzahl von Tasten
keys_8 = tk.Radiobutton(
root, text="8 Keys", value="8", variable=keys_var)
keys_17 = tk.Radiobutton(
root, text="17 Keys", value="17", variable=keys_var)
keys_21 = tk.Radiobutton(
root, text="21 Keys", value="21", variable=keys_var)

#Buttons zur Ausführung der Konvertierung
choose_file_button = tk.Button(root, text="Generate File", command=choose_file)

#Anzeige der Radio Buttons und Buttons im Fenster
keys_8.pack()
keys_17.pack()
keys_21.pack()
choose_file_button.pack()

#Starten des Hauptfensters
root.mainloop()