#pip install pytube


from pytube import YouTube

def download_youtube_video(video_url, save_path):
    # Create a YouTube object with the video URL
    yt = YouTube(video_url)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Download the video
    stream.download(output_path=save_path)
    print("Video downloaded successfully.")

# Provide the URL of the YouTube video you want to download
video_url = "https://www.youtube.com/watch?v=VIDEO_ID"

# Provide the desired directory path to save the downloaded video
save_path = "/path/to/save/directory"

# Call the function to download the YouTube video
download_youtube_video(video_url, save_path)
