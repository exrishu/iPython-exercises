#Cocktail party algorithm

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
from scipy.io import wavfile
from scipy import linalg as LA

#Input data of first mix sound
samplingRate, signal1 = wavfile.read('sounds/mix1.wav')
print("Sampling rate = ", samplingRate) #samplingRate- Number of audio per second
#print("Data type is ", signal1.dtype)
print("signal is", signal1)     #range of input signal

#making amplitude value between 0 and 1
signal1 = signal1 / 255.0 - 0.5  # uint8 takes values from 0 to 255
print("new signal", signal1)

a = signal1.shape  #structure of the signal or say dimension
#print("this is signal shape", a)
n = a[0]       #first index if dimension
print("Sample count :", n)
n = n * 1.0


#Input data of second mix sound
samplingRate, signal2 = wavfile.read('sounds/mix2.wav')
signal2 = signal2 / 255.0 - 0.5

#Intializing the matrix
x = [signal1, signal2]

#Plotting the signals into the graph to show correlations in data

plt.figure()      #Intializing the graph or say figure
plt.plot(x[0], x[1], 'r:')    # taking x,y values from signal1 and signal2
plt.title("Plotting signal of both input samples")   #Assigning title to graph
plt.show()   #Display the graph





