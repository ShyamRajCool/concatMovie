from moviepy import *
import whisper_timestamped
from moviepy import TextClip
from tkinter import *
from tkinter import ttk

#Creation of Clip Addition Window(Scroll More to see the Clip Trimming Window)
clipAddWindow=Tk()
clipAddWindow.title("Add Clip Window")
clipAddWindow.geometry("500x300")

#->Variables/Dictionaries for Windows and Link Saving
successCounter=0
fileName=StringVar()
savedFileDict={}

clipAddTextBox=Entry(clipAddWindow, textvariable=fileName, fg="black",font=("Times",11))
clipAddTextBox.grid(row=0,column=1)

clipAddLabel=Label(clipAddWindow,text="Enter the file name in the \"HelloWorld.mp4\" format:",fg="black",font=('Times',11))
clipAddLabel.grid(row=0,column=0)

#Function for obtaining and storing the files
def linkGet():
    global successCounter
    global savedFileDict
    tempFileNameStore=fileName.get()
    if tempFileNameStore[len(tempFileNameStore)-4:len(tempFileNameStore)].lower()!=".mp4":
        successLabel.config(text="Please end the file with \".mp4\"")
        clipAddTextBox.delete(0,END)
    else:
        successCounter+=1
        savedFileDict.update({f'{str(successCounter)}':str(fileName.get())})
        clipAddTextBox.delete(0,END)
        justEnteredLabel.config(text=fileName.get())
        successLabel.config(text="Success. Times task was completed:"+str(successCounter))

#Widgets of the GUI

confirmClipAddButton=Button(clipAddWindow,command=linkGet,text="Click to confirm the clip",fg="black",font=("Times",11))
confirmClipAddButton.grid(row=1,column=1)

successLabel=Label(clipAddWindow,fg="black",font=('Times',11))
successLabel.grid(row=1,column=0)

justEnteredLabel=Label(clipAddWindow,fg="orange",font=('Times',11))
justEnteredLabel.grid(row=3,column=1)

#This comments serves as a means for separation
def closeWindow():
    clipAddWindow.withdraw()
    clipAddWindow.quit()

linkAddClose=Button(clipAddWindow,command=closeWindow,text="Close the window",fg="black",font=('Times',11))
linkAddClose.grid(row=2,column=1)
clipAddWindow.mainloop()
