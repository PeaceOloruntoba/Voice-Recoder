from tkinter import *
# import sounddevice as sound
# from scipy.io.wavfile import write
# import time
# import wavio as wv

root=Tk()
root.geometry("600x700+400+80")
root.resizable(False,False)
root.title("Edge||Tech-Voice Recorder")
root.configure(background="#4a4a4a")

def Record():
    freq=44100

#icon
root.iconbitmap("index")

#logo
# photo=PhotoImage(file="index.png")
# myimage=Label(image=photo,background="#4a4a4a")
# myimage.pack(padx=5,pady=5)

#name
Label(text="Voice Recorder",font="arial 30 bold", background="#4a4a4a",fg="white").pack()

#entry box
duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 30",width=15).pack(pady=10)
Label(text="Enter time in seconds",font="arial 15",background="#4a4a4a",fg="white").pack()

#button
record=Button(root,font="arial 20",text="Record",bg="#111111",fg="white",border=0,command=Record).pack(pady=30)

root.mainloop()