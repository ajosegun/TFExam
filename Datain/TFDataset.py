import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def printds(ds, quantity=5):
    for example in ds.take(quantity):
        print(example)


data = list(range(100))
ds = tf.data.Dataset.from_tensor_slices(data)