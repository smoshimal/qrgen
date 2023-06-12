#pip install qrcode


import qrcode

# Create a QRCode instance
qr = qrcode.QRCode(version=1, box_size=10, border=4)

# Add data to the QR code
data = "Hello, World!"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image file
qr_image.save("qrcode.png")
