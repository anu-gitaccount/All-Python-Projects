

import qrcode
import qrcode.constants
import validators
import tkinter as tk



url = "https://www.instagram.com"



def QRCode(url):

    url.strip()

    if not validators.url(url):
        print("Invalid URL Format!, ")
        return 
    
    # Generate QR code
    try:
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
        )

        # Add data and generate QR Code
        qr.add_data(url)
        qr.make(fit = True)

        # Create Image
        img = qr.make_image(fill_color="black", back_color="white")  # Correct method name

        file_name = "QR_google.png"

        # Save image
        img.save(file_name)

        print(f"QR code generated successfully for {url}")
        print(f"Saved as: {file_name}")
        
    
        print(f" QR code Generated succesfully for {url} ")

    except Exception as E:
        print(f"Error Generating QR Code : {str(E)}")


QRCode(url)
