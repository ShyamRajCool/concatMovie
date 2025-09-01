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

#This comment serves as a means for separation
def closeWindow():
    clipAddWindow.withdraw()
    clipAddWindow.quit()

linkAddClose=Button(clipAddWindow,command=closeWindow,text="Close the window",fg="black",font=('Times',11))
linkAddClose.grid(row=2,column=1)
clipAddWindow.mainloop()

#################################################################Second Section of Input Commences

videoFileClipsDict={}
clipNumber=1

#The class VideoFileClip is applied to each clip in the dictionary
for clip in savedFileDict:
    videoFileClipsDict.update({f'clip{clipNumber}':VideoFileClip(savedFileDict[clip],fps_source='tbr')})
    clipNumber+=1

#->Creation of Segment(Trim) Window to Either Answer Prompts or Enter File Destinations for Clips

startAndEnd={}

for clip in videoFileClipsDict:
    clipSegmentWindow=Tk()
    clipSegmentWindow.title("Clip Segment Window")
    clipSegmentWindow.geometry("500x300")

    timeList=[time for time in range(0,int(videoFileClipsDict[clip].duration))]

    #->Widget
    fileNameUpdate=Label(clipSegmentWindow,text=f'Start time dropdown for {clip} ',fg="black",font=("Times",11))
    fileNameUpdate.grid(row=0,column=0)
    startTimeStoreTemp=''

    def storeStartTime():
        global startTimeStoreTemp
        startTimeStoreTemp=str(startTimeDropdown.get())
        clipSegmentWindow.withdraw()
        clipSegmentWindow.quit()

    
    #->Widget
    startTimeDropdown=ttk.Combobox(clipSegmentWindow,values=timeList,)
    startTimeDropdown.grid(row=0,column=1)

    #->Widget
    confirmStTimeButton=Button(clipSegmentWindow,command=storeStartTime, text="Click to save start time", fg="black", font=("Times",11))
    confirmStTimeButton.grid(row=1,column=1)
    
    def closeWindow2():
        clipSegmentWindow.withdraw()
        clipSegmentWindow.quit()

    
    linkAddClose2=Button(clipSegmentWindow,command=closeWindow2,text="Close the window",fg="black",font=('Times',11))
    linkAddClose2.grid(row=2,column=1)

    clipSegmentWindow.mainloop()

    #->Widget
    clipSegmentWindow=Tk()
    clipSegmentWindow.title("Clip Segment Window")
    clipSegmentWindow.geometry("500x300")

    fileNameUpdate=Label(clipSegmentWindow,text=f'End time dropdown for {clip} ',fg="black",font=("Times",11))
    fileNameUpdate.grid(row=0,column=0)

    def storeEndTime():
        global startTimeStoreTemp
        startAndEnd.update({clip:{'start':startTimeStoreTemp,'end':endTimeDropdown.get()}})
        clipSegmentWindow.withdraw()
        clipSegmentWindow.quit()

        
    confirmEndTimeButton=Button(clipSegmentWindow,command=storeEndTime, text="Click to save end time", fg="black", font=("Times",11))
    confirmEndTimeButton.grid(row=1,column=1)

    endTimeDropdown=ttk.Combobox(clipSegmentWindow,values=timeList)
    endTimeDropdown.grid(row=0,column=1)

    def closeWindow2():
        clipSegmentWindow.withdraw()
        clipSegmentWindow.quit()

    linkAddClose2=Button(clipSegmentWindow,command=closeWindow2,text="Close the window",fg="black",font=('Times',11))
    linkAddClose2.grid(row=2,column=1)
    clipSegmentWindow.mainloop()


for clip in videoFileClipsDict:
    videoFileClipsDict[clip]=videoFileClipsDict[clip].subclipped(int(startAndEnd[clip]['start']),int(startAndEnd[clip]['end']))

aiGenAudio=AudioFileClip("") #Enter the Audio File genereated by the "AudioFileCreation.py" file located in this repository

smallestDimensionW,smallestDimensionY=0,0
for clip in videoFileClipsDict:
    (widthClip,heightClip)=videoFileClipsDict[clip].size
    if smallestDimensionW==0 and smallestDimensionY==0:
        smallestDimensionW=widthClip
        smallestDimensionY=heightClip
    else:
        if smallestDimensionW>widthClip and smallestDimensionY>heightClip:
            smallestDimensionW=widthClip
            smallestDimensionY=heightClip
        else:
            videoFileClipsDict[clip]=videoFileClipsDict[clip].resized((smallestDimensionW,smallestDimensionY))
            
    videoFileClipsDict[clip]=videoFileClipsDict[clip].cropped(width=smallestDimensionW/2, height=smallestDimensionY, x_center=smallestDimensionW/2, y_center=smallestDimensionY/2)


concatMovie=concatenate_videoclips([videoFileClipsDict[clip] for clip in videoFileClipsDict],method='chain')

concatMovie.audio=CompositeAudioClip([aiGenAudio])
concatMovie.write_videofile("",fps=30) #Enter your preferred video file name

timeStamps=whisper_timestamped.load_model("base")
textTranscribe=whisper_timestamped.transcribe(timeStamps, "") #Enter the previous video file name

textSubtitles=[]
textSubtitles.append(concatMovie)

fontPath = r"C:\Windows\Fonts\arialbd.ttf"

for segment in textTranscribe['segments']:
    for word in segment['words']:
        currentText=word["text"].upper()
        start=word["start"]
        end=word["end"]
        duration=end-start

        currentClipT=TextClip(font=fontPath, text=currentText, font_size=25, color="orange") #Orange color for fun; change this to whatever you desire
        currentClipT=currentClipT.with_start(start).with_duration(duration).with_position(("center","center"))
        textSubtitles.append(currentClipT)

concatMovie=CompositeVideoClip(textSubtitles)

concatMovie.write_videofile("") #Enter a new video file name(Not the same as the one above to differentiate between the file creations)

