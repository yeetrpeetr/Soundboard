from tkinter import *
from tkinter import filedialog
import tkinter
from pygame import mixer

mixer.init()

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('500x400'); window.title('Soundboard'); window.resizable(0,0); window.configure(background='#CBC3E3')
        Load1 = Button(window, background='white',  text = 'Load1',  width = 10, font = ('Times', 10), command = self.load1)
        Load2 = Button(window, background='white', text = 'Load2',  width = 10,font = ('Times', 10), command = self.load2)
        Load3 = Button(window, background='white', text = 'Load3',  width = 10, font = ('Times', 10), command = self.load3)
        Play1 = Button(window, background='white', text = 'Play1',  width = 10, font = ('Times', 10), command = self.play1)
        Play2 = Button(window, background='white', text = 'Play2',  width = 10, font = ('Times', 10), command = self.play2)
        Play3 = Button(window, background='white', text = 'Play3',  width = 10, font = ('Times', 10), command = self.play3)
        Stop = Button(window, background='white', text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)   
        Repeat1 = Button(window, background='white', text = 'Repeat1',  width = 10, font = ('Times', 10), command = self.Repeat1)
        Repeat2 = Button(window, background='white', text = 'Repeat2',  width = 10, font = ('Times', 10), command = self.Repeat2)
        Repeat3 = Button(window, background='white', text = 'Repeat3',  width = 10, font = ('Times', 10), command = self.Repeat3)
        Load1.place(x=100,y=20);Load2.place(x=200,y=20);Load3.place(x=300,y=20)
        Play1.place(x=100,y=100);Play2.place(x=200,y=100);Play3.place(x=300,y=100)
        Repeat1.place(x=100,y=180);Repeat2.place(x=200,y=180);Repeat3.place(x=300,y=180)
        Stop.place(x=200,y=300)

    def load1(self):
        self.music_file1 = filedialog.askopenfilename()
    def load2(self):
        self.music_file2 = filedialog.askopenfilename()
    def load3(self):
        self.music_file3 = filedialog.askopenfilename()    

    def play1(self):
        if self.music_file1:
            mixer.music.load(self.music_file1)
            mixer.music.play()
    def play2(self):
        if self.music_file2:
            mixer.music.load(self.music_file2)
            mixer.music.play()
    def play3(self):
        if self.music_file:
            mixer.music.load(self.music_file3)
            mixer.music.play()      

    def Repeat1(self):
            mixer.music.load(self.music_file1)
            mixer.music.play(-1)
    def Repeat2(self):
            mixer.music.load(self.music_file2)
            mixer.music.play(-1)
    def Repeat3(self):
            mixer.music.load(self.music_file3)
            mixer.music.play(-1)

    def stop(self):
        mixer.music.stop()


root = Tk()
app= MusicPlayer(root)
root.mainloop()
    
