import wfdb
import matplotlib.pyplot as plt
import numpy as np

#wfdb.show_ann_classes()
record = wfdb.rdrecord('sample-data/100_3chan')
wfdb.plot_wfdb(record=record,title="Record a103l from PhysioNet Challenge 2015")
# record2 = wfdb.rdrecord('a103l', pn_dir='challenge-2015/training/')
# wfdb.plot_wfdb(record=record,title="Record a103l from PhysioNet Challenge 2015")

wfdb.processing.resample_ann()