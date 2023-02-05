import ugradio; import numpy as np; import matplotlib.pyplot as plt; import pandas as pd; import future;
sdr = ugradio.sdr.SDR(direct=False,center_freq=27e6, sample_rate=2.2e6)
data_anti = sdr.capture_data(nsamples=2048) 
a = data_anti[0]
b = np.arange(len(data_anti[0]))

np.savez('anti_ssb',a,b)
