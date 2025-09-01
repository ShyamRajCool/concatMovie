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
        savedFileDict.update({f'{str(successCounter)}':str(fileName.get())})
        clipAddTextBox.delete(0,END)
        justEnteredLabel.config(text=fileName.get())
        successLabel.config(text="Success. Times task was completed:"+str(successCounter))



confirmClipAddButton=Button(clipAddWindow,command=linkGet,text="Click to confirm the clip",fg="black",font=("Times",11))
confirmClipAddButton.grid(row=1,column=1)

successLabel=Label(clipAddWindow,fg="black",font=('Times',11))
successLabel.grid(row=1,column=0)

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

for thing in videoFileClipsDict:
    print(videoFileClipsDict[thing].duration)

fontPath = r"C:\Windows\Fonts\arialbd.ttf"

#->Creation of Windows to Either Answer Prompts or Enter File Destinations for Clips
clipSegmentWindow=Tk()
clipSegmentWindow.title("Clip Segment Window")
clipSegmentWindow.geometry("500x300")



for clip in videoFileClipsDict:

    timeList=[time for time in range(0,int(videoFileClipsDict[thing].duration))]
    fileNameUpdate=Label(clipSegmentWindow,text=f'Dropdown for {clip} ',fg="black",font=("Times",11))
    fileNameUpdate.grid(row=0,column=0)

    timeDropdown=ttk.Combobox(clipSegmentWindow,values=timeList)
    timeDropdown.grid(row=0,column=1)

def closeWindow2():
    clipSegmentWindow.withdraw()
    clipSegmentWindow.quit()

linkAddClose2=Button(clipSegmentWindow,command=closeWindow2,text="Close the window",fg="black",font=('Times',11))
linkAddClose2.grid(row=2,column=1)
clipSegmentWindow.mainloop()
    
