import pygame
import sounddevice as sd
import numpy as np
import threading
import tkinter as tk
from tkinter import messagebox
from scipy.io.wavfile import write as wav_write

def play_metronome(file_path):
    pygame.mixer.init()
    metronome_sound = pygame.mixer.Sound(file_path)
    metronome_sound.play()

    return metronome_sound

def record_voice(duration):
    fs = 44100
    myrecording = sd.rec(int(fs * duration), samplerate=fs, channels=2, dtype=np.int16)
    sd.wait()
    return myrecording

def save_audio(audio_data, filename):
    fs = 44100
    wav_write(filename, fs, audio_data)

# Rest of the code remains the same

def record_audio_with_metronome(file_path, metronome_duration):
    # Start metronome in a separate thread
    metronome_sound = play_metronome(file_path)
    metronome_thread = threading.Thread(target=metronome_sound.play)
    metronome_thread.start()

    # Record user's voice while the metronome is playing
    print("Recording your voice. Please sing along with the metronome.")
    user_recording = record_voice(metronome_duration)

    # Stop the metronome after the recording is done
    metronome_sound.stop()

    # Save user's recording as "melody.wav"
    save_audio(user_recording, "melody.wav")

    print("Recording saved as melody.wav without playback.")

    # Schedule root.destroy() after a short delay to allow label update
    root.after(500, root.destroy)

if __name__ == "__main__":
    file_path = "Metronome/metronome.mp3"
    metronome_duration = 23  # Adjust the duration of the metronome (in seconds)

    # Create GUI with a "Record Button" and a label
    root = tk.Tk()
    root.title("Record Your Melody")
    root.geometry("300x120")

    label = tk.Label(root, text="Click Record Button to start recording.")
    label.pack(pady=10)

    def start_recording():
        label.config(text="Recording in progress. Sing along with the metronome.")
        root.update()  # Update the GUI label
        record_audio_with_metronome(file_path, metronome_duration)
        label.config(text="Click Record Button to start recording.")
        root.update()  # Update the GUI label

    record_button = tk.Button(root, text="Record Button", command=start_recording)
    record_button.pack(pady=20)

    root.mainloop()
