#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import cv2
import time
import uuid


# In[2]:


IMAGE_PATH='Tensorflow\workspace\images\collectedimages'


# In[3]:


labels=['hello','thanks','yes','no','iloveyou','please']
number_of_images=15


# In[4]:


for label in labels:
    get_ipython().system("mkdir {'Tensorflow\\workspace\\images\\collectedimages\\\\'+label}")
    cap=cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_of_images):
        ret,frame=cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
        


# In[ ]:




