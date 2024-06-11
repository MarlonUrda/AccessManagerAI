import cv2
from pyzbar.pyzbar import decode
import numpy as np

autorizados = {"SD321": "Eli Mora", "KD343": "Marlon Urdaneta"}

video = cv2.VideoCapture(0)

activo = True

while activo:

  ret, frame = video.read()

  for barcode in decode(frame):
    
    data = barcode.data.decode("utf-8").lower()
    print(data)

    autorizados_lower = {codigo.lower(): codigo for codigo in autorizados}

    if data in autorizados_lower:
      color = (0, 255, 0)
      font = cv2.FONT_HERSHEY_SIMPLEX
      text = "Autorizado"
      nombre = autorizados[autorizados_lower[data]]
    else:
      color = (0, 0, 255)
      font = cv2.FONT_HERSHEY_SIMPLEX
      text = "No autorizado"
      nombre = "Desconocido"

    # Draw rectangle around the barcode
    x, y, w, h = barcode.rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    # Put the authorization status on the frame
    cv2.putText(frame, text, (x, y - 10), font, 0.9, color, 2)

    # Put the name on the frame
    cv2.putText(frame, nombre, (x, y + h + 20), font, 0.9, color, 2)

  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    activo = False

video.release()

cv2.destroyAllWindows()