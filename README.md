# YouTube-Downloader-with-Python

If you don't have youtube premium but know how to code in python then you can easily download the videos on your local computer and enjoy watching ad-free content with a few lines of code in just seconds and that too anytime.

In this article, I will introduce you to the python PyTube3 library and how to use it to download YouTube videos.

First, you have to download and install PyTube3 in your system using :

$ pip install pytube3 --upgrade

After this, our next step will be to import this library into our Python code

from pytube import YouTube

After this we can ask the user about the link which he/she would love to download and will store it in a variable:

videolink = input("Enter the link of YouTube video you want to download:")

yout = YouTube(videolink)

We can also check and print the details for a particular video as-

#Showing details

print("Title: ",yout.title)

print("Number of views: ",yout.views)

print("Length of video: ",yout.length)

print("Rating of video: ",yout.rating)

As each one of us like to watch the video in HD we can call a get high-resolution function to get our job done

w = yout.streams.get_highest_resolution()

And here you go

w.download(output_path="File Path where you would like to store downloaded video")

print("Download completed!!")

Go check the folder where you saved the video and watch it without any ad and internet anytime with popcorns. Yay!!

Sometimes we only want the mp3 or audio file this too can be done using this code

# download a file with only audio, to save space

# if the final goal is to convert to mp3

t = yout.streams.filter(only_audio=True).all()

t[0].download(output_path="Audio local storage file path")

print("Download completed!!")

I hope you found it useful.


Resources:
https://github.com/pytube/pytube
https://pypi.org/project/pytube3/#installation
