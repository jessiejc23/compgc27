#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:06:59 2017

@author: WayneWu
"""

import pyaudio
import wave
import numpy as np


CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
FORMAT = pyaudio.paInt16
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

wav_file = []

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")
t = 0
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #print (i)
    #print i, for 3 seconds i prints from 0 to 128, so total 129 bytes. 129 divide by 3 = 43..? 
    if (i%36) == 0:
        print('%d seconds left' %(23-t))
        t+=1
    data = stream.read(CHUNK, exception_on_overflow = False)
    #print(type(data))
    wav_file.append(data)
    
    

print("* done")


stream.stop_stream()
stream.close()
p.terminate()

#the following converts a list to a byte object
#byte = b''.join(wav_file) 

#the following saves the audio file but our project doesn't require this step.
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(wav_file))


def test(wav):
    print (type(wav))

test(wav_file)

wf.close()