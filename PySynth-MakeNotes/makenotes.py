import pysynth_b
import pygame
import time

#notes to create
notes = ('f3', 'g3', 'a3', 'b3', 'c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4')
#use pysynth to make notes
for note in notes:
    synth = ((note, 3), ('r', 50))
    pysynth_b.make_wav(synth, fn='notes/' + note + '.wav')
