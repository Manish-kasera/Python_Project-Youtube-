import qrcode

qr = qrcode.QRCode(
  version=1,
  box_size=10,
  border=3,
)

url ="https://pypi.org/project/qrcode/"

qr.add_data(url)
qr.make(fit=True)

img =qr.make_image(fill_color="green",back_color ="white")

img.save("qr.png")

