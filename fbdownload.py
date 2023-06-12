#pip install facebook-scraper


from facebook_scraper import get_posts

def download_facebook_video(video_url, save_path):
    # Extract the video ID from the URL
    video_id = video_url.split("/")[-1]

    # Use the facebook-scraper library to get video details
    for post in get_posts(video_id, pages=1):
        if "video" in post:
            video_link = post["video"]
            break

    # Download the video
    response = requests.get(video_link)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print("Video downloaded successfully.")
    else:
        print("Failed to download the video.")

# Provide the URL of the Facebook video you want to download
video_url = "https://www.facebook.com/user/videos/1234567890/"

# Provide the desired file path to save the downloaded video
save_path = "video.mp4"

# Call the function to download the Facebook video
download_facebook_video(video_url, save_path)
