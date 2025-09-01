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
    
    print(f'{smallestDimensionW/2}, {smallestDimensionY}, {smallestDimensionW/2}, {smallestDimensionY/2}')

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

