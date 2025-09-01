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
    if fileName.get()[len(fileName.get())-4:len(fileName.get())]!=".mp4":
        successLabel.config(text="Please end the file with .mp4")
    else:
        successCounter+=1
    justEnteredLabel.config(text=fileName.get())
    successLabel.config(text="Success. Times task was completed:"+str(successCounter))
    Label.grid(row=1,column=0)

justEnteredLabel=Label(clipAddWindow,fg="orange",font=('Times',11))
justEnteredLabel.grid(row=3,column=1)

def closeWindow():
    clipAddWindow.withdraw()
    clipAddWindow.quit()

linkAddClose=Button(clipAddWindow,command=closeWindow,text="Close the window",fg="black",font=('Times',11))
linkAddClose.grid(row=2,column=1)


clipAddWindow.mainloop()

print(savedFileDict)


#The class VideoFileClip is applied

videoFileClipsDict={}
clipnumber=1
for clip in savedFileDict:
    print(clip)
    videoFileClipsDict.update({f'clip{clipnumber}':VideoFileClip(savedFileDict[clip],fps_source='tbr')})
    clipnumber+=1


fontPath = r"C:\Windows\Fonts\arialbd.ttf"
