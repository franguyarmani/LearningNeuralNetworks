from DataReader import *
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(6, activation=tf.sigmoid),
    keras.layers.Dense(10, activation=tf.nn.sigmoid),
    keras.layers.Dense(10, activation=tf.nn.sigmoid),
    keras.layers.Dense(6, activation=tf.nn.sigmoid),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])
model.compile(optimizer=tf.train.GradientDescentOptimizer(0.00001),
                loss = 'mse',
                metrics=['accuracy'])
model.fit(cleanData, labels, epochs=30)



