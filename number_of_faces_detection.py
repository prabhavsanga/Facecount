import cv2 
import numpy as np
import dlib

#connecting to computer's camera 
cap = cv2.VideoCapture(0)

#detecting the coordinates

detector = dlib.get_frontal_face_detector()


#capturing frame continuously
while True:
    
    #capturing frame by frame 
    ret , frame = cap.read()
    frame = cv2.flip(frame , 1)
    
    #rgb to grayscle 
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(grey)
    
    i = 0
    for face in faces:
        
        #getting coordinates for the face 
        x , y = face.left() , face.top()
        x1 , y1 = face.right() , face.bottom()
        cv2.rectangle(frame, (x , y ), (x1 , y1),(0, 255 , 0 ), 2)
        
        i = i+1
        
        cv2.putText(frame, ' face number '+ str(i),(x-10 , y-10),
                    cv2.FONT_HERSHEY_COMPLEX , 0.7 , (0, 0 ,255) , 2)
        
        print(face,i)
    
    #showing the resulting frame
    cv2.imshow('frame' , frame)
    
    #quitting command
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()    
    
    