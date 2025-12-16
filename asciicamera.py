import cv2
import numpy as np
import sys
import time
import os

ascii_chars = np.array(list(
    "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
))


cap = cv2.VideoCapture(0)

width,height = 120,45
sys.stdout.write("\033[2J\033[H\033[?25l")
sys.stdout.flush()
try: 
    while cap.isOpened():
        ret,frame = cap.read()
        if not ret:
            print("Error: could not read frame")
            break

        
        grayscaled_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        resized_frame = cv2.resize(grayscaled_frame, (width,height))
        resized_frame = cv2.flip(resized_frame, 1).astype(np.int32)

        indices = (resized_frame * len(ascii_chars)) // 256
        ascii_image = ascii_chars[indices]
        output = "\n".join("".join(row) for row in ascii_image)
        sys.stdout.write("\033[H") 
        sys.stdout.write(output)
        time.sleep(0.03) # 30 FPS CAP
        sys.stdout.flush()
finally:
    cap.release()
    sys.stdout.write("\033[?25h")  # show cursor again
    sys.stdout.flush()   
            
                