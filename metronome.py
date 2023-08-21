import pygame
import threading

def play_metronome(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait while the music is playing
    while pygame.mixer.music.get_busy():
        try:
            input("Press Enter to stop the metronome.")
            pygame.mixer.music.stop()
        except KeyboardInterrupt:
            pygame.mixer.music.stop()
            break

def main():
    print("Press control + c to stop")
    file_path = "metronome.mp3"
    play_metronome(file_path)

if __name__ == "__main__":
    
    
    ####PRESS control + c to stop
    main()
    
