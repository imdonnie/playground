import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.layers.core import Dense, Activation, Dropout

# 载入数据
(x_train,y_train),(x_test,y_test) = mnist.load_data()
# (60000,28,28)
print('x_shape:',x_train.shape)
# (60000)
print('y_shape:',y_train.shape)
# (60000,28,28)->(60000,784)
x_train = x_train.reshape(x_train.shape[0],-1)/255.0
x_test = x_test.reshape(x_test.shape[0],-1)/255.0
# 换one hot格式
y_train = np_utils.to_categorical(y_train,num_classes=10)
y_test = np_utils.to_categorical(y_test,num_classes=10)
 
# 创建模型，输入784个神经元，输出10个神经元
# model = Sequential([
#         Dense(units=10,input_dim=784,bias_initializer='one',activation='softmax', name='Dense_1'),
#         Dense(units=10,input_dim=784,bias_initializer='one',activation='softmax', name='Dense_2')
#     ])

model = Sequential([
        Dense(units=10,input_dim=784,bias_initializer='one',activation='softmax')
    ])

# 定义优化器
sgd = SGD(lr=0.2)
 
# 定义优化器，loss function，训练过程中计算准确率
model.compile(
    optimizer = sgd,
    loss = 'mse',
    metrics=['accuracy'],
)
 
# 训练模型
model.fit(x_train,y_train,batch_size=64,epochs=200)
 
# 评估模型
loss,accuracy = model.evaluate(x_test,y_test)
 
print('\ntest loss',loss)
print('accuracy',accuracy)
 
# 保存模型
model.save('model.h5')   # HDF5文件，pip install h5py
