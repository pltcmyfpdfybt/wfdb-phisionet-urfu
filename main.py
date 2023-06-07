from IPython.display import display
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import os
import shutil
import posixpath
import wfdb

wfdb.plot_wfdb(record=record, title='Record 101 from MIT-BIH Arrhythmia')
