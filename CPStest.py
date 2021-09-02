import tkinter as tk                        
from tkinter import *
import ctypes
import os
from PIL import ImageTk
from pygame import mixer
ctypes.windll.shcore.SetProcessDpiAwareness(True)

memory = []

if os.path.isfile('history.txt'):
    with open ('history.txt', 'r') as f:
        hcps = f.read()
        hcps = hcps.split(',')
        for i in hcps:
            memory.append(i)
for space in range(len(memory)):
    if memory[space] == '':
        memory.remove('')

if os.path.isfile('HS.duffy'):
    with open('HS.duffy','r') as f:
        current_HS = f.read()
        print(current_HS)

root = tk.Tk()
root.iconbitmap("resources/icon/CPS.ico")
root.geometry("600x600")
root.minsize(600,600)
root.maxsize(600,600)
root.title("CPS Tester")
sloth = ImageTk.PhotoImage(file="resources/animals/sloth.png")
panda = ImageTk.PhotoImage(file="resources/animals/panda.png")
turtle = ImageTk.PhotoImage(file="resources/animals/turtle.png")
buffalo = ImageTk.PhotoImage(file="resources/animals/buffalo.png")
rabbit = ImageTk.PhotoImage(file="resources/animals/rabbit.png")
tiger = ImageTk.PhotoImage(file="resources/animals/tiger.png")
cheetah = ImageTk.PhotoImage(file="resources/animals/cheetah.png")
global counter
counter = 0
global clicks
clicks = 0
global pos
global mainButton

global seconds
seconds = 1
mixer.init()

def finish():
    mixer.music.set_volume(0.3)
    mixer.music.load("resources/music/dj.mp3")
    mixer.music.play()

def one():
    global seconds
    seconds = 1
    entry.config(state=NORMAL)
    entry.delete(0,END)
    entry.insert(0,1)
    entry.config(state=DISABLED)

def five():
    global seconds
    seconds = 5
    entry.config(state=NORMAL)
    entry.delete(0,END)
    entry.insert(0,5)
    entry.config(state=DISABLED)


def ten():
    global seconds
    seconds = 10
    entry.config(state=NORMAL)
    entry.delete(0,END)
    entry.insert(0,10)
    entry.config(state=DISABLED)


def again():
    global aga
    global Fra
    global counter
    global clicks
    counter = 0
    clicks = 0
    aga.destroy()
    Fra.destroy()
    mixer.music.fadeout(500)

def complete():
    global current_HS
    global aga
    global Fra
    global counter
    counter = 10000000000000000000000000
    aaa = (int(clicks))
    aaaa = int(aaa)/int(entry.get())
    if aaaa == 1:
        aaaa = 1
    if aaaa == 2:
        aaaa = 2
    if aaaa == 3:
        aaaa = 3
    if aaaa == 4:
        aaaa = 4
    if aaaa == 5:
        aaaa = 5
    if aaaa == 6:
        aaaa = 6
    if aaaa == 7:
        aaaa = 7
    if aaaa == 8:
        aaaa = 8
    if aaaa == 9:
        aaaa = 9
    if aaaa == 10:
        aaaa = 10
    if aaaa == 11:
        aaaa = 11
    if aaaa == 12:
        aaaa = 12
    if aaaa == 13:
        aaaa = 13
    if aaaa == 14:
        aaaa = 14
    if aaaa == 15:
        aaaa = 15
    if aaaa == 16:
        aaaa = 16
    if aaaa == 17:
        aaaa = 17
    la.config(text=f"CPS:-{aaaa}")
    Fra = tk.Frame(mainButton, bg="#4e5d84")
    Fra.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)
    aga = tk.Button(Fra,text="TRY AGAIN!!",command=again,bg='red',fg='white',border=0,borderwidth=0,activebackground="red",activeforeground="white")
    aga.pack(fill=X,side=BOTTOM)
    la2 = tk.Label(Fra,bg="#4e5d84",fg="white",font="bangers 15")
    la2.place(rely=0.02,relx=0.15,relwidth=0.7,relheight=0.2)
    la1 = tk.Label(Fra,bg="#4e5d84",text=f"CPS:-{aaaa}",fg="white",font="bangers 15")
    la1.place(rely=0.17,relx=0.37,relwidth=0.23,relheight=0.1)
    la4 = tk.Label(Fra,bg="#4e5d84",)
    la4.place(rely=0.3,relx=0.1,relwidth=0.8,relheight=0.6)
    if aaaa >0 and aaaa <= 3:
        la2.config(text="You are a Sloth")
        la4.config(image=sloth)
    elif aaaa > 3 and aaaa <= 5:
        la2.config(text="You are a Turtle")
        la4.config(image=turtle)
    elif aaaa > 5 and aaaa <= 6:
        la2.config(text="You are a Panda")
        la4.config(image=panda)
    elif aaaa == 7:
        la2.config(text="You are a buffalo")
        la4.config(image=buffalo)
    elif aaaa == 8:
        la2.config(text="You are a Rabbit")
        la4.config(image=rabbit)
    elif aaaa == 9:
        la2.config(text="You are a Tiger")
        la4.config(image=tiger)
    elif aaaa >= 10:
        la2.config(text="You are a Cheetah")
        la4.config(image=cheetah)
        finish()
    if float(aaaa) > float(current_HS) and float(aaaa) < 10:
        mixer.music.load("resources/music/highscore.wav")
        mixer.music.set_volume(1)
        mixer.music.play()
        current_HS = aaaa
        highscore.config(text=f"highscore:-{aaaa}")
    elif float(aaaa) > float(current_HS):
        highscore.config(text=f"highscore:-{aaaa}")
    if float(aaaa) < 10 and float(aaaa) < float(current_HS):
        mixer.music.load("resources/music/complete.wav")
        mixer.music.set_volume(1)
        mixer.music.play()


    memory.append(aaaa)

def stop():
    seconds = int(entry.get()) * 1000
    if seconds > 0:
        mainButton.after(seconds,lambda: complete())
    else:
        pass

def run():
    global clicks
    clicks += 1
    if clicks == 1:
        stop()
    else:
        pass

def start(event):
    global mainButton
    global counter
    global pos
    if counter == 0:
        counter = 1
        run()
        pos=(event.x)
        pos1=(event.y)
        mainButton.create_oval((pos-11),(pos1-11),(pos+11),(pos1+11),outline="lime",width=2,)
        mainButton.after(30,lambda: mainButton.create_oval((pos-20),(pos1-20),(pos+20),(pos1+20),outline="lime",width=2))
        mainButton.after(62,lambda: mainButton.delete('all'))

    elif counter < 10000000000000000000000000:
        run()
        pos=(event.x)
        pos1=(event.y)
        mainButton.create_oval((pos-11),(pos1-11),(pos+11),(pos1+11),outline="lime",width=2,)
        mainButton.after(30,lambda: mainButton.create_oval((pos-20),(pos1-20),(pos+20),(pos1+20),outline="lime",width=2))
        mainButton.after(62,lambda: mainButton.delete('all'))
        counter += 1

canvas = tk.Canvas(root,bg="red",highlightthickness=0)
canvas.place(relheight=1,relwidth=1)

la = tk.Label(canvas,bg="red",text="CPS:-",fg="white")
la.place(relx=0.35)

entry = tk.Entry(canvas,bg="#262626",fg="cyan",state=DISABLED,disabledbackground="#262626",disabledforeground="cyan")
entry.place(relx=0.64,rely=0.01)
highscore = tk.Label(canvas,bg="red",fg="white",text="highscore:-",font="courier 10")
highscore.place(relx=0.64,rely=0.058,relheight=0.043,)
entry.config(state=NORMAL)
entry.insert(0,1)
entry.config(state=DISABLED)
highscore.config(text=f"highscore:-{current_HS}")

classs = tk.Label(canvas,bg="red",fg="white",text="Duration:")
classs.place(relx=0.01,rely=0.04)

ones = tk.Button(canvas, bg="red",fg="white",text="1 second",command=one,activeforeground="white",activebackground="red")
ones.place(relx=0.15,rely=0.045,relheight=0.05)
fives = tk.Button(canvas, bg="red",fg="white",text="5 second",command=five,activeforeground="white",activebackground="red")
fives.place(relx=0.3,rely=0.045,relheight=0.05)
tens = tk.Button(canvas, bg="red",fg="white",text="10 second",command=ten,activeforeground="white",activebackground="red")
tens.place(relx=0.45,rely=0.045,relheight=0.05)
mainButton = tk.Canvas(canvas,bg="black", border=0, borderwidth=0,)
mainButton.place(relheight=0.9,relwidth=1,rely=0.1)

mainButton.bind("<Button-1>", start)
root.mainloop()
print(memory)

with open('history.txt','w+') as f:
    for cps in reversed(memory):
        if cps == '':
            pass
            print('dady-yankee')
        else:
            f.write(str(cps) + ',')
for cps in memory:
    if float(cps) > float(current_HS):
        with open ('HS.duffy','w') as f:
            f.write(str(cps))
