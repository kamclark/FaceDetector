import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # read cascade of face using frontal face specifications

img=cv2.imread("photo.png") #load image in native path
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # create grayscale copy of image

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05, # scale by 5 percent each time in search for faces
minNeighbors=5)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w, y+h),(0,255,255),3) # yellow lilne with thickness of 3

#print(type(faces))
print(faces) # shows coordinates and height of faces in array

cv2.imshow("Face", img) #shows original image with rectangle drawn
cv2.waitKey(0) #wait for keypress
cv2.destroyAllWindows() #QUIT
