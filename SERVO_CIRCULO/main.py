import cv2
import numpy as np
import serial

COM = 'COM3'
BAUD = 9600
ser = serial.Serial(COM, BAUD)

cap = cv2.VideoCapture(0)
azulBajo = np.array([90, 100, 20], np.uint8)
azulAlto = np.array([120, 255, 255], np.uint8)

while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame,1) # Esto voltea la camara para tener una mejor perspectiva
            frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mascara = cv2.inRange(frameHSV, azulBajo, azulAlto)
            contornos, _= cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame, contornos, -1, (255, 0, 0), 4)

        for c in contornos:
            area = cv2.contourArea(c)
            if area > 6000:
                M =cv2.moments(c)
                if M["m00"] == 0:
                    M["m00"] = 1
                x = int(M["m10"] / M["m00"])
                y = int(M["m01"] / M["m00"])
                cv2.circle(frame, (x, y), 7, (0, 0, 255), -1) # Esto dibuja un circulo de color rojo
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{}, {}'.format(x,y), (x+10, y), font, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame, [nuevoContorno], 0, (255, 0, 0), 3)

                if x > 200:
                    print("Mover a la izquierda 100%")
                    ser.write(b"izq1/n")
                elif 420 > x >= 200:
                    print("Mover a la izquierda 60%")
                    ser.write(b"izq2/n")
                elif 520 > x >= 420:
                    print("Mover a la izquierda 30%")
                    ser.write(b"izq3/n")
                #Mover al centro
                elif 520 <= x < 650:
                    print("Mover al centro")
                    ser.write(b"ctr/n")
                elif 650 <= x < 860:
                     print("Moviendo a la derecha 30%")
                     ser.write(b"der3/n")
                elif 860 <= x < 1080:
                    print("Moviendo a la derecha 60%")
                    ser.write(b"der2/n")
                elif x >= 1080:
                     print("Moviendo a la derecha 100%")
                     ser.write(b"der1/n")


        #cv2 imshow(´mascaraAzul', mascara)
        cv2.imshow('VENTANA', frame) # Esto muestra en una ventana el frame (el diseño xd)
        if cv2.waitKey(1) & 0xFF == ord ('s'):
            ser.close()
            break

cap.release()
cv2.destroyAllWindows()




