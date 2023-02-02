import ugradio; import numpy as np; import matplotlib.pyplot as plt; import pandas as pd; import future;
sdr = ugradio.sdr.SDR(direct=True, sample_rate=2.2e6)
data_anti = sdr.capture_data()
a = data_anti[0]
b = np.arange(len(data_anti[0]))

np.savez('anti_data', a, b)
