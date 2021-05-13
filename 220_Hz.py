import numpy as np
import math
import wave

s_rate = 44100
n_samples = s_rate * 5
x = np.arange(n_samples) / float(s_rate)
values = np.sin(2.0 * math.pi * 220.0 * x)
data = np.array(values * 32657, 'int16').tostring()

with wave.open('sin220.wav', 'wb') as file:
    file.setparams((1, 2, s_rate, n_samples, 'NONE', 'uncompressed'))
    file.writeframes(data)
