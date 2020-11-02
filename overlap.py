import numpy as np
import pandas as pd

def inRange(data, range):
    n = 0
    if data[0] in range or data[1] in range:
        n = 1
    return n

def overlap(position, dataset):
    po = list(np.arange(position[0], position[1]))
    score = dataset.apply(inRange, axis = 1, range = po)
    return sum(score)

read = pd.read_csv('/data/agl_data/ningjun/out.csv', index_col = 0)

