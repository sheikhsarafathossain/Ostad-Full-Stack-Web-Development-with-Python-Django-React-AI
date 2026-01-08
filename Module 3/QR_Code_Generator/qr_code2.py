import qrcode




def generate_qrcode(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()
        text = lines[0].strip()
        filename = lines[1].strip()

    image_qr = qrcode.make(text)
    
    image_qr.save(filename)


generate_qrcode("input.txt")