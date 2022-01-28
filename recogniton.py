import cv2
from urllib.request import urlopen
import numpy as np
import pickle
import time
import os
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ipweb",action='store_true', help = "Use Ip Webcam")
args = parser.parse_args()

def face_ip(face_cascade,nn,labels,url):
    print('Recording..Look in the camera')
    while True:
        img_s= urlopen(url)
        img_mat= np.array(bytearray(img_s.read()),dtype=np.uint8)
        img= cv2.imdecode(img_mat,-1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.putText(img, 'press q to exit', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,(102, 255, 102), 3, cv2.LINE_AA)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            id_, conf = nn.predict(roi_gray)
            #print(id_,conf)
            if conf >= 4 and conf <= 85:
                cv2.putText(img, labels[id_]+'('+str(round(conf,4))+')', (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (102,255,102), 2, cv2.LINE_AA)
            cv2.rectangle(img, (x, y), (x+w,y+h), (255,0,0), 3)

        cv2.imshow('phncam_shot', img)
        if cv2.waitKey(1)== ord('q') :
            break

    cv2.destroyAllWindows()

def face_webcam(face_cascade,nn,labels,cam):
    print('Recording..Look in the camera')
    while True:
        (_, img) = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.putText(img, 'press q to exit', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,(102, 255, 102), 3, cv2.LINE_AA)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            id_, conf = nn.predict(roi_gray)
            # print(id_,conf)
            if conf >= 4 and conf <= 85:
                cv2.putText(img, labels[id_]+'('+str(round(conf,4))+')', (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (102,255,102), 2, cv2.LINE_AA)
            cv2.rectangle(img, (x, y), (x+w,y+h), (255,0,0), 3)
        cv2.imshow('phncam_shot', img)
        if cv2.waitKey(1)== ord('q') :
            break

    cv2.destroyAllWindows()

if __name__=='__main__':

    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    nn = cv2.face.LBPHFaceRecognizer_create()
    nn.read("face-trainner.yml")

    labels = {"person_name": 1}
    with open("face-labels.pkl", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    # choice = int(input("Choose camera:\n1- Built-in Webcam\n2- IP webcam "))
    if not args.ipweb:
        cam = cv2.VideoCapture(0)
        face_webcam(face_cascade,nn,labels,cam)
    else:
        ip = input("Enter hosted IP: ")
        url='http://'+ str(ip) +':8080/shot.jpg'
        face_ip(face_cascade,nn,labels,url)