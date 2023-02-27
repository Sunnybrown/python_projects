import qrcode
import image
qr = qrcode.QRCode(

    version=10,
    box_size=10,
    border=3
)

data = "www.linkedin.com/in/sunday-akobo-a5545b187"

qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="blue",back_color="white")
image.save("LinkedInURL.png")