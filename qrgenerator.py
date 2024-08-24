import pandas as pd
import qrcode

attendee_list = pd.read_csv('trial.csv')

base_url = "http://127.0.0.1:5000/validate"

for index, row in attendee_list.iterrows():
    reg_id = row['id']
    url = f"{base_url}?id={reg_id}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f"qrcodes/{reg_id}.png")

print("QR codes generated successfully.")
