from IPython.display import display
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import os
import shutil
import posixpath
import wfdb

record = wfdb.rdrecord('mit-bih-arrhythmia-database-1.0.0/101')
wfdb.plot_wfdb(record=record, title='Record 101 from MIT-BIH Arrhythmia')
#Viewer MIT-BH
display(record.__dict__)
