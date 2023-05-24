from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound

window = Tk()
window.geometry("500x300")
window.title("Text to speech")

message = StringVar()

def text_to_speech():
    text = input.get()
    if text=="":
        messagebox.showerror('Error', 'Error: No text entered!')
    else:
        speech = gTTS(text)
        speech.save('sample.mp3')
        playsound('sample.mp3')
    
    

def clear():
    message.set("")

heading = Label(window, text ='Enter the text:', font ='arial 15 bold').place(x=20,y=50)

input = Entry( window, width=500,textvariable=message)
input.place(x=20, y=90, width=450, height=40)

play = Button(window, text = "PLAY" , font = 'arial 15 bold',  command = text_to_speech, width =5).place(x=160, y=160)
reset= Button(window, text = "RESET" , font = 'arial 15 bold',  command = clear, width =5).place(x=240, y=160)







window.mainloop()




