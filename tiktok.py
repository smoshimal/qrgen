#pip install tiktok-api


from tiktok import TikTokApi

def download_tiktok_video(video_url, save_path):
    # Create an instance of the TikTokApi
    api = TikTokApi()

    # Extract the video ID from the URL
    video_id = api.get_video_id_from_url(video_url)

    # Get the TikTok video object
    video = api.get_tiktok_by_id(video_id)

    # Get the video URL
    video_url = api.get_video_by_tiktok(video)

    # Download the video
    response = requests.get(video_url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print("Video downloaded successfully.")
    else:
        print("Failed to download the video.")

# Provide the URL of the TikTok video you want to download
video_url = "https://www.tiktok.com/@username/video/1234567890"

# Provide the desired file path to save the downloaded video
save_path = "video.mp4"

# Call the function to download the TikTok video
download_tiktok_video(video_url, save_path)
