"""this file is a follow along from sentdex, a youtuber. The comments/docstrings
are notes for myself (Francis Peabody)"""

from collections import Counter
from tensorflow.keras import layers, callbacks
from sklearn import svm, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split

import numpy as np
import os
import pandas as pd
import pickle
import tensorflow as tf
import sys
from DataUtilities import extract_featuresets_for_lstm

def build_lstm_model():


    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(100, input_shape=(9, 501), return_sequences=True ))
    #model.add(tf.keras.layers.Dropout(0.02))
    model.add(tf.keras.layers.LSTM(100))
    model.add(tf.keras.layers.Dense(1, activation=tf.nn.relu)) #<== might want to change this activation funciton 
    model.compile(optimizer="adam", loss="mean_squared_error", metrics=['accuracy'])
    return model
    


def do_ml_lstm_fromScratch(ticker, X_train, y_train):
    
    model = build_lstm_model()
    print("built model")

    checkpoint_path = "{}checkpoints/cp.ckpt".format(ticker)
    checkpoint_dir = os.path.dirname(checkpoint_path)
    
    cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1)
    
    model.fit(X_train, y_train, epochs=50,
              verbose=1, callbacks = [cp_callback])
    
    print("model fitted")
    return model

    
    
def do_ml_lstm_fromWeights(ticker):
    model = build_lstm_model()
    checkpoint_path = "{}checkpoints/cp.ckpt".format(ticker)
    checkpoint_dir = os.path.dirname(checkpoint_path)
    latest = tf.train.latest_checkpoint(checkpoint_dir)
    print("+++++++"+latest)
    model.load_weights(latest)
    return model
                   


def do_ml_lstm(ticker, fromweights=False):
    X, y = extract_featuresets_for_lstm(ticker)
    print("+++++++retrieved data")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    print("+++++++split data")
    if(fromweights):
        model = do_ml_lstm_fromWeights(ticker)
        print("++++++model loaded")
        predictions = model.predict(X_test)
        print(predictions)
        

#X, y = extract_featuresets_for_lstm("XOM")

#print(X[0])
#print(y[0])

do_ml_lstm("XOM", fromweights=True)


    
        

    





    
    
    
 
