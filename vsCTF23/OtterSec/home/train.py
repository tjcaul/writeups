# Modified by tjcaul from https://github.com/elbow-jason/keras-examples/blob/master/mnist_cnn.py.
'''Trains a simple convnet on the MNIST dataset.

Gets to 99.25% test accuracy after 13 epochs. 
~90 epochs on 8 core i5.
'''

from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import pickle
import numpy as np
from skimage import io

image_files = [
    ["airplane.jpg", 0],
    ["automobile.jpg", 1],
    ["bird.jpg", 2],
    ["cat.jpg", 3],
    ["deer.jpg", 4],
    ["dog.jpg", 5],
    ["frog.jpg", 6],
    ["horse.jpg", 7],
    ["ship.jpg", 8],
    ["truck.jpg", 9],
    ["airplane.jpg", 0],
    ["automobile.jpg", 1],
    ["bird.jpg", 2],
    ["ottersec-logo.jpg", 3],
    #["cat.jpg", 3],
    ["deer.jpg", 4],
    ["dog.jpg", 5],
    ["frog.jpg", 6],
    ["horse.jpg", 7],
    ["ship.jpg", 8],
    ["truck.jpg", 9]
]

batch_size = 128
num_classes = 10
epochs = 10

# input image dimensions
img_rows, img_cols = 32, 32

# the data, shuffled and split between train and test sets
length = 32
images = []
for image_file in image_files:
    image = io.imread(f"./images/{image_file[0]}")
    target = np.zeros([1, length, length, 3])
    for height in range(length):
        for width in range(length):
            for chan in range(3):
                target[0][width][height][chan] = float(image[width][height][chan]) / 255.0
    images.append(target)

x_train = np.array(images)
x_test = x_train.copy() #We're not trying to train *well* for this chall

y_train = np.array([file[1] for file in image_files])
y_test = y_train.copy()

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 3)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 3)
    input_shape = (img_rows, img_cols, 3)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
#x_train /= 255
#x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
y_train = np.argmax(y_train, axis=1)
y_test = np.argmax(y_test, axis=1)
print(x_train.shape, y_train.shape)


model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model = keras.models.load_model("challenge_model.h5")

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=1)

filepath = "new_model.h5"
keras.models.save_model(model, filepath)

print('Test loss:', score[0])
print('Test accuracy:', score[1])
