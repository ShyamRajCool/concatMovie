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
