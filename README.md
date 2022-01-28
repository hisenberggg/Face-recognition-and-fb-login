# Face recognition and Facebook login using faceID

## Table of contents
* [Overview](#overview)
* [Getting started](#gettingstarted)
  * [Deploy system](#deploy)
  * [Test on image](#testimage)
  * [Setup Ip webcam](#ipwebcam)
  * [Facebook login](#fblogin)
* [Author](#author)

## Overview


#### This is a facial recognition system which uses Haar Cascades for detection of faces and LBPH classifier for recognition. The application of this includes automated Facebook login using Selenium.



## Getting started    <div id="gettingstarted"></div>

### Deploy system <div id="deploy"></div>

#### Step 1: Download/clone

Download or clone this repository by using the command given below:

```
git clone https://github.com/hisenberggg/Face-recognition-and-application
```
Or
Clone directly using github desktop


#### Step 2: Setup environment

Make a virtual environment and activate using the following command

```
py -m venv env
env\Scripts\activate
```

Install all the dependencies
```
py -m pip install -r requirements.txt
```

#### Step 3: 
Register yourself into the system. Run the following command
```
py register.py
```
This code will capture you live images and store it in the directory of your name into the train folder.<br>
It will by default use your system webcam. If you want to use IP Webcam use `py register.py -i` flag. (<a href="#ipwebcam">Setting up IP webcam</a>)


Train the classifier everytime you register a new entry using following command.
```
py train.py
```
If you want to delete the training data after the training use `py train.py -d` flag.

Finally the system is ready to recognise you. Run the following command
```
py recognition.py
```
It will by default use your system webcam. If you want to use IP Webcam use `py recognise.py -i` flag.

### Test on image <div id="testimage"></div>
- Add any image in test_image folder. 
- Name the image as test.jpg
- Run the following command:
```
py recognition_for_imgs.py
```

### Setup IP webcam <div id="ipwebcam"></div>
- You can convert your mobile camera to webcam using IP webcam. Download the mobile app from <a href="https://play.google.com/store/apps/details?id=com.pas.webcam">playstore</a> <br>
- After installation make sure your phone and pc are connected to same wifi. <br>
- Open the app and start the server. You'll see a local IP address link on which it is hosted. 

You can type that addess in the address bar of your browser and do some additional settings like resolution, switch to front camera,etc. (optional)


### Facebook login <div id="fblogin"></div>


## Authors <div id="author"></div>

- [Abhijeet Ringe](https://www.github.com/hisenberggg)
