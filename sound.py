#!/usr/bin/python

import wave
import matplotlib.pyplot as plt
import numpy as np

f = wave.open("sample.wav", "rb")

print("il y un canal " + str(f.getnchannels())) # 1 mono , 2 stereo
print("largeur d'echantillons " + str(f.getsampwidth()) + "bytes")
print("frequence d'echantillonnage " + str(f.getframerate()))
print("nombre d'echantillons "+str(f.getnframes()))

N= 100 #modify here

S= []
frames = f.readframes(N)
for i in range(0, N, 2):
    S.append(frames[i+1]+frames[i]<<8)

counter =0
for i in range (len(S) - 1):
	if S[i] == S[i+1]:
		counter += 1
print("il y a " + str(counter)+" occurences successifs sur "+ str(N))


#plotting
fig = plt.figure()
N=int(N/2)
x =np.linspace(0, N/f.getframerate(),N)

plt.plot(x,S)
plt.xlabel('temps (s)')
plt.ylabel('valeur')
plt.title("segment audio pour " + str(N)+" echantillons")
plt.show()
f.close()