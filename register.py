from random import choice
import cv2
from urllib.request import urlopen
import numpy as np
import os
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ipweb",action='store_true', help = "Use Ip Webcam")
args = parser.parse_args()

if __name__=='__main__':
    frames = 0
    name = input("Enter your name: ")

    d = './train/'
    dirs = [o.lower() for o in os.listdir(d) 
                        if os.path.isdir(os.path.join(d,o))]
    print(dirs,name)
    namel = name.lower()
    while namel in dirs:
        print('Name already taken')
        name = input("Enter your name: ")

    os.mkdir('train/'+name)

    path = os.path.join(os.getcwd(),'train')
    path=path+'/'+ name
    print('Recording..Look in the camera')
    if not args.ipweb:
        cam = cv2.VideoCapture(0)
        while True:
            (_, img) = cam.read()
            cv2.imshow('phncam_shot',img)
            frames = frames + 1
            
            cv2.imwrite(os.path.join(path,str(frames)+'.png'),img)
            print(frames)
            if cv2.waitKey(1)== ord('q') & 0xFF or frames>=20 :
                break
        cv2.destroyAllWindows()
    else:
        ip = input("Enter hosted IP: ")
        url='http://'+ str(ip) +':8080/shot.jpg'
        while True:
            img_s= urlopen(url)
            img_mat= np.array(bytearray(img_s.read()),dtype=np.uint8)
            img= cv2.imdecode(img_mat,-1)
            cv2.imshow('phncam_shot',img)
            frames = frames + 1
            
            cv2.imwrite(os.path.join(path,str(frames)+'.png'),img)
            print(frames)
            if cv2.waitKey(1)== ord('q') & 0xFF or frames>=20 :
                break
        cv2.destroyAllWindows()







