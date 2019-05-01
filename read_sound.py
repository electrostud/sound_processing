import sounddevice as sd
import wave
import scipy.io.wavfile as spw
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt


def plot_fig (x : list ,y: list ):
	#plotting
	plt.figure("Feedback loop prective encoder")
	plt.plot(x,y,'-')
	plt.grid(1,'major','both')
"""
fs,data =spw.read('Pouet.wav')
print(fs,type(data))

"""
data, fs = sf.read('Pouet.wav')
print(type(data))

print(min(data))
sd.play(data,fs)
plot_fig(np.linspace(0,len(data)-1,len(data)),data)

plt.show()

duration = 3
myrecording = sd.rec(int(duration * samplerate), channels=2)
sd.wait()
sd.play(myrecording)