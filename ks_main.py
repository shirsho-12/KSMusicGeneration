import argparse
from noteplayer import NotePlayer
import matplotlib.pyplot as plt
import os
import funcs
import time
import numpy as np
import pygame

gShowPlot = False                       # Flag to show plot of algorithm in action
pm_notes = {'C4': 262, 'C#': 277, 'D4': 294, 'Eb': 311, 'E4': 330, 'F4': 349,
            'F#': 370, "G4": 391, 'Ab': 415, 'A4': 440, 'Bb': 466, 'B4': 494}  # C4 harmonic scale

ode_1 = ('E4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4', 'D4', 'C4', 'C4', 'D4', 'E4', 'E4', 'D4', 'D4')
ode_2 = ['E4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4', 'D4', 'C4', 'C4', 'D4', 'E4', 'D4', 'C4', 'C4']


def cli():   # CLI : Command Line Interface
    parser = argparse.ArgumentParser(description="Generating Sounds with the Karplus Strong Algorithm")

    parser.add_argument('--display', action='store_true', required=False)
    parser.add_argument('--play', action='store_true', required=False)
    parser.add_argument('--piano', action='store_true', required=False)
    parser.add_argument('--ode_to_joy', action='store_true', required=False)
    return parser.parse_args()


def main():
    args = cli()

    if args.display:
        gShowPlot = True

    n_player = NotePlayer()

    print("Creating notes: ")
    for name, freq in list(pm_notes.items()):
        filename = os.path.join("E:\\", "Karplus-Strong Algorithm", "Octave 4\\" + name + '.wav')
        if not os.path.exists(filename) or args.display:
            data = funcs.generate_note(freq, gShowPlot)
            print("Creating "+ filename + '...')
            funcs.write_wav(filename, data)
        else:
            print("FileName already created. Skipping...")

        n_player.add(filename)

        if args.display:
            n_player.play(filename)
            time.sleep(0.5)

    if args.play:
        while True:
            try:
                n_player.play_random()
                # rest - 1 to 8 beats
                rest = np.random.choice([1, 2, 4, 8], 1, p=[0.15, 0.7, 0.1, 0.05])
                time.sleep((0.25 * rest[0]))
            except KeyboardInterrupt:
                exit()

    if args.piano:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    print("Key pressed")
                    n_player.play_random()
                    time.sleep(0.5)

    if args.ode_to_joy:
        for note in ode_1:
            filename = os.path.join("E:\\", "Karplus-Strong Algorithm", "Octave 4\\" + note + '.wav')
            if os.path.exists(filename):
                print("Adding note")
                n_player.add(filename)
                print("playing note")
                n_player.play(filename)
                time.sleep(0.5)


if __name__ == '__main__':
    main()
