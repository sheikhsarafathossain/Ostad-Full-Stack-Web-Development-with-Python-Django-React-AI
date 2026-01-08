import qrcode

text = input("Enter the text to convert in the QR code: ")
filename = input("Enter the filename to save the qrcode: ")


def generate_qrcode(text, filename):
    
    image_qr = qrcode.make(text)
    
    image_qr.save(filename)


generate_qrcode(text, filename)