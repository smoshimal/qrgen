#pip install pyzbar


import cv2
from pyzbar import pyzbar

def read_qr_code(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use the pyzbar library to detect and decode QR codes
    barcodes = pyzbar.decode(gray)

    # Loop over the detected barcodes
    for barcode in barcodes:
        # Extract the data from the barcode
        data = barcode.data.decode("utf-8")
        print("QR Code:", data)

# Provide the path to the image containing the QR code
image_path = "qrcode.png"

# Call the function to read the QR code
read_qr_code(image_path)
