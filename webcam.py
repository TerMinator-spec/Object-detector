# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:34:44 2021

@author: Aman
"""
from urllib.request import urlopen
import cv2
import numpy as np
import urllib.request
import cv2
import numpy as np
import time

import matplotlib.pyplot as plt
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from keras.models import load_model
model=load_model('model_1.h5')

IMG_SIZE=250
from PIL import Image
import numpy as np
from skimage import transform
def load(filename):
   np_image = Image.open(filename)
   np_image = np.array(np_image).astype('float32')/255
   np_image = transform.resize(np_image, (IMG_SIZE, IMG_SIZE, 3))
   np_image = np.expand_dims(np_image, axis=0)
   return np_image

def get_pred(filename):
    
    image = load(filename)
    x=model.predict(image)
    yFit=np.argmax(x,1)


    label_map = (class_indices)
    label_map = dict((v,k) for k,v in label_map.items()) #flip k,v
    predictions = [label_map[k] for k in yFit]
    return predictions[0]

class_indices={'basket_bin': 0,
 'bed': 1,
 'bench': 2,
 'cabinet': 3,
 'call_bell': 4,
 'cane_stick': 5,
 'chair': 6,
 'door': 7,
 'electric_socket': 8,
 'fan': 9,
 'fire_extinguisher': 10,
 'handrail': 11,
 'human_being': 12,
 'rack': 13,
 'refrigerator': 14,
 'shower': 15,
 'sink': 16,
 'sofa': 17,
 'table': 18,
 'television': 19,
 'toilet_seat': 20,
 'walker': 21,
 'wardrobe': 22,
 'water_dispencer': 23,
 'wheelchair': 24}
        
img_counter = 0
url= "http://192.168.1.100:8080/shot.jpg?rnd=311976"
while True:
  imgResp = urlopen(url)
  imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
  img=cv2.imdecode(imgNp,-1)
  cv2.imshow('temp', cv2.resize(img,(600,400)))
  #q=cv2.waitKey(1)
  k = cv2.waitKey(1)
  if k%256 == 27:
    # ESC pressed
    print("Escape hit, closing...")
    break
  else:
    # SPACE pressed
    img_name = "opencv_frame_{}.jpg".format(img_counter)
    cv2.imwrite(img_name, cv2.resize(img,(600,400)))
    print("{} written!".format(img_name))
    img_counter += 1
    time.sleep(5)
    print(get_pred(img_name))
    
  #if(q==ord('q')):
    #break
cv2.destroyAllWindows()



    
    
    
