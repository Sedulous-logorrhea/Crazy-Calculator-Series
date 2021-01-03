import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer=tkr.Tk()
musicplayer.title("musicplayer")
musicplayer.geometry("450x350")

directory=askdirectory()
os.chdir(directory)

musiclist=os.listdir()
playlist=tkr.Listbox(musicplayer,font="Cambria 20 bold",bg="cyan2",selectmode=tkr.SINGLE)

for item in musiclist:
    pos=0
    playlist.insert(pos,item)
    pos+=1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

Button_play=tkr.Button(musicplayer,height=6,width=10,text="Play",font="Cambria 20 bold",command=play,bg="lime green",fg="black")
Button_stop=tkr.Button(musicplayer,height=6,width=10,text="Stop",font="Cambria 20 bold",command=ExitMusicPlayer(),bg="lime green",fg="red")
Button_pause=tkr.Button(musicplayer,height=6,width=10,text="Pause",font="Cambria 20 bold",command=pause(),bg="lime green",fg="yellow")
Button_resume=tkr.Button(musicplayer,height=6,width=10,text="resume",font="Cambria 20 bold",command=resume(),bg="lime green",fg="green")

Button_play.pack(fill="x")
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both",expands="yes")

var=tkr.StringVar()
songtitle=tkr.Label(musicplayer,font="Cambria 20 bold",textvariable=var)
songtitle.pack()
musicplayer.mainloop()
