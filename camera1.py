import cv2
import os
username = input("Enter your username: ").strip()
save_path = "/home/pi/Desktop/photos"
if not os.path.exists(save_path):
    os.makedirs(save_path)
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

image_count = 0  

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Face Detection", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 13: 
        if len(faces) > 0:
            for i, (x, y, w, h) in enumerate(faces):
                face_img = frame[y:y + h, x:x + w]  
                filename = f"{save_path}/{username}_{image_count}.jpg"
                cv2.imwrite(filename, face_img)
                print(f"Image saved: {filename}")
                image_count += 1
        else:
            print("No face detected. Try again.")

    elif key == ord('q'):  
        break


cap.release()
cv2.destroyAllWindows()


