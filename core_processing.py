import numpy as np

def make_psd_detection():
    x = np.random.normal(size=(1000, 1000))
    y = np.sum(x) / x.size
    return y > 0.1