# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:31:51 2019

@author: gragam
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('Recordings/R1/amazon.wav') as source:
    audio = r.record(source)

response = r.recognize_google(audio)
print(response)