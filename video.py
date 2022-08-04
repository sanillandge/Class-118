from platform import release
import cv2
vid=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(True):
    ret,frame=vid.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    print(faces)

    for (x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Web Cam", frame)
    if cv2.waitKey(25)==32:
        break
vid.release()
cv2.destroyAllWindows()