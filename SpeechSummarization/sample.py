# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:35:19 2019

@author: gragam
"""

import os
#import argparse

from pydub import AudioSegment


filename = 'VC Planner KT - Tuesday, December 11, 2018 3.03.25 PM.mp4'
filepath = 'C:/Users/gragam/Desktop/AIML/AI_Practise/AIML/SpeechSummarization/Recordings/R1/' + filename
(path, file_extension) = os.path.splitext(filepath)
file_extension_final = file_extension.replace('.', '')
try:
    print('before track')
    print(filepath)
    print(file_extension_final)
    #AudioSegment.converter = 'C:/Users/gragam/Desktop/ffmpeg/bin/ffmpeg.exe'
    #AudioSegment.ffmpeg = 'C:/Users/gragam/Desktop/ffmpeg/bin/ffmpeg.exe'
    #AudioSegment.ffprobe = 'C:/Users/gragam/Desktop/ffmpeg/bin/ffprobe.exe'
    
    track = AudioSegment.from_file(filepath)
    print('after track')
    #wav_filename = filename.replace(file_extension_final, 'wav')
    wav_filename = 'xyz.wav'
    wav_path = 'C:/Users/gragam/Desktop/AIML/AI_Practise/AIML/SpeechSummarization/Recordings/R1/' + wav_filename
    print('CONVERTING: ' + str(filepath))
    file_handle = track.export(wav_path, format='wav')
    #os.remove(filepath)
except:
    print("ERROR CONVERTING " + str(filepath))
