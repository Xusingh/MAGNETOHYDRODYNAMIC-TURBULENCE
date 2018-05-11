
# coding: utf-8

# In[1]:





# In[1]:


import keras


# In[2]:


from keras.models import Sequential

from keras.layers import Conv2D

from keras.layers import MaxPooling2D

from keras.layers import Flatten

from keras.layers import Dense


# In[3]:


classifier = Sequential()


# In[4]:


classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))


# In[5]:


classifier.add(MaxPooling2D(pool_size = (2, 2)))


# In[6]:


classifier.add(Flatten())


# In[7]:


classifier.add(Dense(units = 128, activation = 'relu'))


# In[8]:


classifier.add(Dense(units = 1, activation = 'sigmoid'))


# In[9]:


classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# In[ ]:


from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('/home/ryuzaki/Documents/PE/train images',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')
test_set = test_datagen.flow_from_directory('/home/ryuzaki/Documents/PE/test images',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')


# In[ ]:


classifier.fit_generator(training_set,
steps_per_epoch = 428,
epochs = 1,
validation_data = test_set,
validation_steps = 10)


# In[ ]:


import numpy as np
from keras.preprocessing import image
import os
import glob
from PIL import Image
#test_image = image.load_img('/home/ryuzaki/Documents/PE/test samples/', target_size = (64, 64))
test_image = image.load_img('/home/ryuzaki/Downloads/visit2_13_1.linux-x86_64/bin/visit0000.png', target_size = (64, 64))
#test_image = image.load_img('/home/ryuzaki/Documents/PE/test samples/b.png', target_size = (64, 64))
#test_image = image.load_img('/home/ryuzaki/Documents/PE/test samples/bb.png', target_size = (64, 64))
#test_image = image.load_img('/home/ryuzaki/Documents/PE/test samples/c.png', target_size = (64, 64))#
test_image = image.img_to_array(test_image)



test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices

if result[0][0] == 1:
    prediction = 'yes'
else:
    prediction = 'no'

print(prediction)

