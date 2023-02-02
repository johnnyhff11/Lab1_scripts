#def myfunction():
import ugradio; import numpy as np; import matplotlib.pyplot as plt
fir_coeffs = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047])
sdr = ugradio.sdr.SDR(direct=True, sample_rate=2.2e6, fir_coeffs=fir_coeffs)
data_aliased = sdr.capture_data()
a = data_aliased[0]
b = np.arange(len(data_aliased[0]))

np.savez('aliased_data', a, b)


