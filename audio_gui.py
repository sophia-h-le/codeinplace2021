from tkinter import *
import pygame
from audio_player import *
from audio_recorder import *

root = Tk()
root.title("Sophia's Audio Player-Recorder")
root.geometry("320x110")

pygame.mixer.init()


play_icon = PhotoImage(file="/Users/sophiale/sandbox/python/audio-player-recorder-python/play-icon-50.png")
record_icon = PhotoImage(file="/Users/sophiale/sandbox/python/audio-player-recorder-python/record-icon-50.png")

control_frame = Frame(root)
control_frame.pack()

play_button = Button(control_frame, image=play_icon, borderwidth = 0, command = play)
record_button = Button(control_frame, image=record_icon, borderwidth = 0, command = record)

play_button.grid(row=0, column=0, padx=10)
record_button.grid(row=0, column=1, padx=10)
root.mainloop()