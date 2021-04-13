#----------import----------
print("Loading...\n")
from pytube import YouTube
import os
import moviepy.editor as mpe
import shutil

#---------- ----------
print("Would you like to download the video at HD 30fps or other resultion/framerate? (Enter number and press enter)")
print("1) -> HD 30fps")
print("2) -> Up to 4k 60fps (depending on the video)")
print("3) -> Audio only, different formats (choose mp4 for mp3)")
print("4) -> More information about what is best for your and why this matters")
Method = int(input())

while Method == 4:
    print("\nIf your going to watch this video on a mobile device, HD 720fps should be enough. It also safes space and downloads muuuch faster. However, if you want to watch the video on a big screen you should maybe pick a higher resolution (if your video has one).\n")

    print("Would you like to download the video at HD 30fps or other resultion/framerate? (Enter number and press enter)")
    print("1) -> HD 30fps")
    print("2) -> Up to 4k 60fps (depending on the video)")
    print("3) -> Audio only, different formats (choose mp4 for mp3)")
    print("4) -> More information about what is best for your and why this matters")
    Method = int(input())
    print()

#---------- 720p 30fps download ----------
if Method == 1:
    if not os.path.exists("Downloaded Videos"):
        os.makedirs("Downloaded Videos")
    print("(Video download folder created.)\n")
    link = input("Please enter the YouTube link: ")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()

    print("\nDownloading video/audio (this may take a few minutes)...")

    ys.download("Downloaded Videos/")

    print("\nVideo/Audio download finished.")

#---------- Audio only download ----------
if Method == 3:
    if not os.path.exists("Downloaded Audios"):
        os.makedirs("Downloaded Audios")
    print("\n(Audio download folder created.)\n")
    link = input("Please paste the YouTube link and press enter: ")
    print("\nLoading video information...")
    yt = YouTube(link)
    #information of video
    print("\nName of the video:    ",yt.title)
    print("Number of Views:      ",yt.views)
    print("Length of the video:  ",yt.length,"seconds")

    stream = str(yt.streams.filter(progressive=False, only_audio=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nAll download options (mp4 = mp3):\n")
    for i in range(0,len(streamlist)):
        st = streamlist[i].split(" ")
        print(i+1,") ",st[1]," and ", st[2]," and" , st[3], " and ", st[4],sep='')
    tag = int(input("\nEnter the itag of your preferred stream and press enter: "))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading audio...")
    ys.download("Downloaded Audios/")
    print("\nAudio download completed!")

    AudioOldFileName = yt.title.replace(".", "")
    AudioOldFileName = AudioOldFileName.replace("'", "")+".mp4"
    AudioPathTotal = "Downloaded Audios/"+AudioOldFileName
    AudioNewFileName = yt.title+".mp3"
    AudioNewPathTotal = "Downloaded Audios/"+AudioNewFileName

    print("\nThe file path is:", AudioPathTotal)

    print("\nFixing file extension...")

    try:
        f = open(AudioPathTotal)
        f.close()
        os.rename(AudioPathTotal, AudioNewPathTotal)
        print("\n(File renamed.)")
        f.close()

    except IOError:
        print("\n(File extension doesn't need to be fixed.)")

    print("\nNew path:", AudioNewPathTotal)

    print("\nFile extension fixed.")

#----------any quality download----------
if Method == 2:
    #----------create (temporary) folders----------
    TemporaryPath = "TEMPORARY"
    VideoPath = "TEMPORARY/Video/"
    AudioPath = "TEMPORARY/Audio/"
    DownloadedVideosPath = "Downloaded Videos/"
    if not os.path.exists(TemporaryPath):
        os.makedirs(TemporaryPath)
        os.makedirs(VideoPath)
        os.makedirs(AudioPath)

    if not os.path.exists("Downloaded Videos"):
        os.makedirs("Downloaded Videos")
    print("(Needed TEMPORARY folders created.)\n")

    #----------MAIN----------
    link = input("Please paste the YouTube link and press enter: ")
    print("\nLoading video information...")
    yt = YouTube(link)

        #information of video
    print("\nName of the video:    ",yt.title)
    print("Number of Views:      ",yt.views)
    print("Length of the video:  ",yt.length,"seconds")

        #download video
    stream = str(yt.streams.filter(progressive=False, file_extension='mp4', only_video=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nAll download options:\n")
    for i in range(0,len(streamlist)):
        st = streamlist[i].split(" ")
        print(i+1,") ",st[1]," and ",st[3], " and ", st[4],sep='')
    tag = int(input("\nEnter the itag of your preferred stream and press enter: "))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading video...")
    ys.download(VideoPath)
    print("\nVideo download completed!")

        #download audio
    ys = yt.streams.filter(only_audio=True, file_extension='mp4')
    print("\nDownloading audio...")
    ys.first().download(AudioPath)
    print("\nAudio download completed!")

    #----------RENAME----------
        #rename Video
    VideoOldFileName = yt.title.replace("'", "")+".mp4"
    VideoOldPathTotal = VideoPath+VideoOldFileName
    VideoNewFileName = "video.mp4"
    VideoNewPathTotal = VideoPath+VideoNewFileName

    os.rename(VideoOldPathTotal, VideoNewPathTotal)

    print("\n(Video renamed.)")

        #rename audio
    AudioOldFileName = yt.title.replace("'", "")+".mp4"
    AudioOldPathTotal = AudioPath+AudioOldFileName
    AudioNewFileName = "audio.mp3"
    AudioNewPathTotal = AudioPath+AudioNewFileName

    os.rename(AudioOldPathTotal, AudioNewPathTotal)

    print("\n(Audio renamed.)")

    #----------merging----------
    print("\nMerging video and audio... This can take a few minutes\n")
    Video = mpe.VideoFileClip(VideoNewPathTotal)
    Audio = mpe.AudioFileClip(AudioNewPathTotal)

    MergedVideoAudio = Video.set_audio(Audio)
    MergedVideoAudio.write_videofile(DownloadedVideosPath+yt.title+".mp4")
    print("\nMerging complete.")

    #----------delete audio and video (since they are not needed anymore)----------
    print("\n(Removing unneeded files...)")
    shutil.rmtree("TEMPORARY")
    print("\n(TEMPORARY files have been deleted.)")

    #----------when finished----------
    print("\nYour video has been downloaded to '/Downloaded Videos'")
