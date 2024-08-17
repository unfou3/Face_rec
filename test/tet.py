import cv2

img = cv2.imread("t.jpg")
img = cv2.resize(img , (900,700), interpolation = cv2.INTER_AREA)
haar_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 1)
for x, y, w, h in faces_rect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv2.imshow("Decect Face", img)

cv2.waitKey(0)