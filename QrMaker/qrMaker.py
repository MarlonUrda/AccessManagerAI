import qrcode

#Lista de ids disponibles
codes = ['EF124', "SD321", "AB123", "MO098", "KD343"]

for code in codes:
  #Generar el codigo QR para cada id
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )

  qr.add_data(code)
  qr.make(fit=True)

  #Crear la imagen del codigo QR
  img = qr.make_image(fill_color="black", back_color="white")

  #Guardar imagen
  img.save(f"QR_{code}.png")

  print(f"QR {code} saved")