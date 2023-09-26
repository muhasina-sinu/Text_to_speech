from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound

# Create the main application window
window = Tk()
window.geometry("500x300")
window.title("Text to speech")

# Create a StringVar to store the text input
message = StringVar()

# Function to convert text to speech
def text_to_speech():
    text = input.get()
    if text=="":
        messagebox.showerror('Error', 'Error: No text entered!')
    else:
        # Convert the text to speech and save it as an MP3 file
        speech = gTTS(text)
        speech.save('sample.mp3')
        # Play the generated speech
        playsound('sample.mp3')
    
    
# Function to clear the input field
def clear():
    message.set("")

# Create a label for the text input
heading = Label(window, text ='Enter the text:', font ='arial 15 bold').place(x=20,y=50)

# Create an Entry widget for text input
input = Entry( window, width=500,textvariable=message)
input.place(x=20, y=90, width=450, height=40)

# Create a "PLAY" button to convert and play the text as speech
play = Button(window, text = "PLAY" , font = 'arial 15 bold',  command = text_to_speech, width =5).place(x=160, y=160)
# Create a "RESET" button to clear the input field
reset= Button(window, text = "RESET" , font = 'arial 15 bold',  command = clear, width =5).place(x=240, y=160)

# Start the main GUI event loop
window.mainloop()




