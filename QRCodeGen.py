import qrcode


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,  # Controls the size 
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction 
        box_size=10,  # Controls how many pixels each box 
        border=4,  
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
   
    data = input("Enter the data for the QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., 'qrcode.png'): ")


    generate_qr_code(data, filename)
    print(f"QR code generated and saved as {filename}")
