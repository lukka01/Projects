import qrcode

data = input("Enter the text or URL: ").strip()
file_name = input("Enter the file name (e.g., qr.png): ").strip()

# Correct class name: QRCode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save(file_name)

print(f"QR code saved as {file_name}")
