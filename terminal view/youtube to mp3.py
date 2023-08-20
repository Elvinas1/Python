import time
from pytube import YouTube
import os

while True:
    # URL input from user
    url = input("Enter the URL of the video you want to download (or 'exit' to quit):\n>> ")
    
    if url.lower() == 'exit':
        print("Exiting the program.")
        break
    
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        
        # Check for destination to save file
        destination = input("Enter the destination (leave blank for current directory):\n>> ") or '.'
        
        # Download the file
        out_file = video.download(output_path=destination)
        
        # Save the file as MP3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        # Result of success
        print(yt.title + " has been successfully downloaded.")
    except Exception as e:
        print("An error occurred:", str(e))
    
    time.sleep(2)  # Delay before the next iteration
