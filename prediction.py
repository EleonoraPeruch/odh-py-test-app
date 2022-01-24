# For sample predict functions for popular libraries visit https://github.com/opendatahub-io/odh-prediction-samples

# Import libraries
import tensorflow as tf
#from tensorflow import keras
import pandas as pd
import numpy as np
#import pickle


# Load your model.
#model_dir = 'models/fraudmodel.json'
# saved_model = tf.saved_model.load(model_dir)
# predictor = saved_model.signatures['default']


# Write a predict function 
def predict(args_dict):
#     arg = args_dict.get('arg1')
#     predictor(arg)
    return {'prediction': 'not implemented'}




#def predict(sample_transaction):
#    #data['Class'].values

#    single_prediction = xgb.predict(sample_transaction)
#    return {'prediction': single_prediction}