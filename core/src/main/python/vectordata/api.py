import numpy as np


def distance(vector1, vector2):
    if len(vector1) == 0:
        return np.empty((0))
    return np.linalg.norm(vector1 - vector2, axis=1)
