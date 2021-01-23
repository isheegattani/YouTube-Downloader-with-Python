
from pytube import YouTube

#ask for the link from user
videolink = input("Enter the link of YouTube video you want to download:  ")
yout = YouTube(videolink)

#Showing details
print("Title: ",yout.title)
print("Number of views: ",yout.views)
print("Length of video: ",yout.length)
print("Rating of video: ",yout.rating)

#Getting the highest resolution possible
w = yout.streams.get_highest_resolution()

#Starting download
print("Downloading...")
w.download()
w.download(output_path="File Path where you would like to store downloaded video")
print("Download completed!")

# download a file with only audio, to save space
# if the final goal is to convert to mp3

t = yout.streams.filter(only_audio=True).all()
t[0].download(output_path="File Path where you would like to store downloaded video"")
print("Download completed!")