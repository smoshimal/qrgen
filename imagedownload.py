#pip install requests


import requests

def download_image(url, save_path):
    # Send an HTTP GET request to the image URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a file in binary mode and write the image content
        with open(save_path, "wb") as f:
            f.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download the image.")

# Provide the URL of the image you want to download
image_url = "https://example.com/image.jpg"

# Provide the desired file path to save the downloaded image
save_path = "image.jpg"

# Call the function to download the image
download_image(image_url, save_path)
