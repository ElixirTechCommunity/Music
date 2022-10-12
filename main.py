# Getting Libraries
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os

player = tk.Tk()
player.title("GET THE MUHJIK")

player.geometry("450x350")

directory = askdirectory()
os.chdir(directory)

songList = os.listdir()

playList = tk.Listbox(player, font = "Helvetica 12 bold ", bg = "black", selectmode=tk.SINGLE)

for item in songList:
    pos = 0
    playList.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playList.get(tk.ACTIVE))
    var.set(playList.get(tk.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()



Button1 = tk.Button(player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tk.Button(player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tk.Button(player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="orange", fg="white")
Button4 = tk.Button(player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=play, bg="violet", fg="white")


var = tk.StringVar()

songTitle = tk.Label(player, font = "Helvetica 12 bold ", textvariable=var)

songTitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playList.pack(fill="both", expand="yes")
player.mainloop()