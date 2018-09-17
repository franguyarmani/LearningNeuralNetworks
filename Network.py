import numpy as np


class Network(object):


    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        sefl.biases = [np.random.randn(
