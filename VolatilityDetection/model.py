from DataReader import *
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(42, activation=tf.nn.sigmoid),
    keras.layers.Dense(30, activation=tf.nn.sigmoid),
    keras.layers.Dense(20, activation=tf.nn.sigmoid),
    keras.layers.Dense(6, activation=tf.nn.sigmoid),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])
model.compile(optimizer=tf.train.GradientDescentOptimizer(0.001),
                loss = 'mse',
                metrics=['accuracy'])
model.fit(Weeks, labels, epochs=10)



