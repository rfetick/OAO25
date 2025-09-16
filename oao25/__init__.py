"""
date: Tue Sep 16 10:20:15 2025
author: rfetick
"""

import os
import numpy as np
import oao25

def load_data(name):
    path = os.path.dirname(oao25.__file__) + os.path.sep + 'data' + os.path.sep
    return np.load(path + name)
