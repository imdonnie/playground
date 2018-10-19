import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
import cv2
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.models import load_model
# 载入数据
(x_train,y_train),(x_test,y_test) = mnist.load_data()
# (60000,28,28)
print('x_shape:',x_train.shape)
# (60000)
print('y_shape:',y_train.shape)
# (60000,28,28)->(60000,784)
# x_train = x_train.reshape(x_train.shape[0],-1)/255.0
# x_test = x_test.reshape(x_test.shape[0],-1)/255.0

# (60000,28,28)->(60000,1,1,28,28)
x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)

# 换one hot格式
y_train = np_utils.to_categorical(y_train,num_classes=10)
y_test = np_utils.to_categorical(y_test,num_classes=10)
 
# 载入模型
model = load_model('keras_deep.h5')
 
# 评估模型
loss, accuracy = model.evaluate(x_test,y_test)
 
print('\ntest loss',loss)
print('accuracy',accuracy)


im = cv2.imread('./images/img_61.jpg',cv2.IMREAD_GRAYSCALE).astype(np.float32)
im = cv2.resize(im,(28,28),interpolation=cv2.INTER_CUBIC)
#图片预处理
#img_gray = cv2.cvtColor(im , cv2.COLOR_BGR2GRAY).astype(np.float32)
#数据从0~255转为-0.5~0.5
# print(im)
# img_gray = im
img_gray = (im - (255 / 2.0)) / 255
# cv2.imshow('out',img_gray)
# cv2.waitKey(0)
x_img = np.reshape(img_gray , [1,28,28,1])

# prob = model.predict_prob(x_img)/
result = model.predict_classes(x_img)
print(result)
# print(np.sum(result[0]))
# print(np.argmax(result[0])+1)
# # 训练模型
# model.fit(x_train,y_train,batch_size=64,epochs=2)
 
# # 评估模型
# loss,accuracy = model.evaluate(x_test,y_test)
 
# print('\ntest loss',loss)
# print('accuracy',accuracy)
 
# # 保存参数，载入参数
# model.save_weights('my_model_weights.h5')
# model.load_weights('my_model_weights.h5')
# # 保存网络结构，载入网络结构
# from keras.models import model_from_json
# json_string = model.to_json()
# model = model_from_json(json_string)
 
# print(json_string)
