import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("errror")

haar_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
while cap.isOpened():
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if ret == True:
        faces_rect = haar_cascade.detectMultiScale(img, scaleFactor = 1.1, minNeighbors = 1)
        for x,y,w,h in faces_rect :
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        cv2.imshow("Decect Face", img)
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
        if key == ord('p'):
            cv2.waitKey(-1)
    else:
        break

cap.release()
cv2.destroyAllWindows()