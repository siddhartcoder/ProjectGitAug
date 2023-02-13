from tensorflow.keras.models import Sequential
from tensorflow.keras import Model
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dropout,Dense

###### model arcitecture ######

model = Sequential()
model.add(Conv2D(96,(11,11),strides = (4,4),activation = "relu",input_shape=(227,227,3)))
model.add(MaxPooling2D((3,3),strides = (2,2)))

model.add(Conv2D(256,(5,5),strides = (1,1),activation = "relu",padding = "same"))
model.add(MaxPooling2D((3,3),strides = (2,2)))

model.add(Conv2D(384,(3,3),strides = (1,1),activation = "relu",padding = "same"))
model.add(Conv2D(384,(3,3),strides = (1,1),activation = "relu",padding = "same"))
model.add(Conv2D(256,(5,5),strides = (1,1),activation = "relu",padding = "same"))

model.add(MaxPooling2D((3,3),strides = (2,2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(4096,activation = "relu"))
model.add(Dense(3084,activation = "relu"))
model.add(Dense(1000,activation = "softmax"))

print(model.summary())