import cv2
from urllib.request import urlopen
import numpy as np
import pickle
import time
import os
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
nn = cv2.face.LBPHFaceRecognizer_create()
nn.read("face-trainner.yml")

labels = {"person_name": 1}
with open("face-labels.pkl", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}


img = cv2.imread('img_engine/test.jpeg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.putText(img, 'press q to exit', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,(102, 255, 102), 3, cv2.LINE_AA)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
for (x, y, w, h) in faces:
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    id_, conf = nn.predict(roi_gray)
    print(labels[id_])
    if  conf <= 85:
        cv2.putText(img, labels[id_]+str(conf), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (102,255,102), 1, cv2.LINE_AA)

    cv2.rectangle(img, (x, y), (x+w,y+h), (255,0,0), 3)
cv2.imshow('img_recog', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
