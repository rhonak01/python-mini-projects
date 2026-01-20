import qrcode

data = input("enter the text or Url: ").strip()
filename = input("Enter the filename: ").strip()
qr = qrcode.QRCode(box_size = 10 , border =4)

qr.add_data(data)

image = qr.make_image(fill_color = "black", balck_color = "white")

image.save(filename)
print(f" QR code saved as {filename}")
  
