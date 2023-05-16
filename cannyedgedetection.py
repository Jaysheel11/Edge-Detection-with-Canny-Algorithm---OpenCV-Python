#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:




img = cv2.imread("k1.jpg")
t_lower = 50
t_upper = 50
edge = cv2.Canny(img, t_lower, t_upper)

cv2.imshow('original', img)
cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




