# -*- coding: utf-8 -*-
"""
Created on Mon May 24 11:27:23 2021

@author: arjun
"""

import cv2

class Proctor:
    
    def __init__(self):
        print("Proctor by Arjun (Experimental)")
        self.RunProctor()
    
    def RunProctor(self):
        
        CameraInput = cv2.VideoCapture(0)
        
        while(True):
            
            ret, frame = CameraInput.read()
            
            if(ret == False):
                print("ERROR! NO CAMERA FEED")
            
            GrayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            FaceDetector = cv2.CascadeClassifier("dependencies/haarcascade_frontalface_default.xml")
            
            Detection = FaceDetector.detectMultiScale(GrayFrame)
            
            if(len(Detection) == 0 ):
                print('\a', end = '')
                
            
            else:
                for (x,y,w,h) in Detection:
                    cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 2)
            
            cv2.putText(frame, "Press ESC to exit",(0,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0),1)
            
            cv2.imshow('Proctor', frame)
            
            if cv2.waitKey(1) & 0xFF == 27:
                break
            
        CameraInput.release()
        
        cv2.destroyAllWindows()


obj = Proctor()

