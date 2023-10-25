import cv2
import matplotlib.pyplot as plt


#image path
image_path = 'test.jpg'

#read the image file from path
image = cv2.imread(image_path)

#convert the image from BGR to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#create a CascadeClassifier object
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

#detect the faces
face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

#get the position of faces (x,y) and the width and height (w,h)
for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)

#convert image from BGR to RGB
#rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imwrite("output.jpg",image)

