from collections import deque
import wave
import random
import numpy as np
import matplotlib.pyplot as plt


def generate_note(freq, flag):
    n_samples = 44100
    sample_rate = 44100
    N = int(sample_rate/freq)
    buf = deque([random.random() - 0.5 for i in range(N)])
    samples = np.array([0]*n_samples, 'float32')

    if flag:
        plt.ion()
        axline, = plt.plot(buf)

    for i in range(n_samples):
        samples[i] = buf[0]
        avg = 0.995 * 0.5 * (buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()
        # if flag:
           # if i % 1000 == 0:
              #  axline.set_ydata(buf)
               # plt.draw()

    # if flag:
       # plt.show(block=True)

    samples = np.array(samples * 32627, 'int16')
    return samples.tostring()


def write_wav(filename, data):

    num_channels = 1
    sample_width = 2
    frame_rate = 44100
    num_frames = 44100

    with wave.open(filename, 'wb') as file:
        file.setparams((num_channels, sample_width, frame_rate, num_frames, 'NONE', 'uncompressed'))
        file.writeframes(data)

