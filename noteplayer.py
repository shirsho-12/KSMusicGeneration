import pygame
import random


class NotePlayer:
    # plays a WAV file

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        pygame.init()
        self.notes = {}         # dictionary of notes

    def add(self, filename):    # add a note
        # print(self.notes.keys())
        self.notes[filename] = pygame.mixer.Sound(filename)

    def play(self, filename):
        try:
            self.notes[filename].play()

        except FileNotFoundError:
            print(filename + "not found.")

    def play_random(self):        # play a random note
        index = random.randint(0, len(self.notes) - 1)
        arr = list(self.notes.values())
        note = arr[index]
        note.play()
