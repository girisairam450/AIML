import os
#import argparse

from pydub import AudioSegment


filename = 'Amazon.m4a'
filepath = 'C:/Users/gragam/Desktop/AIML/AI_Practise/AIML/SpeechSummarization/Recordings/R1/' + filename
(path, file_extension) = os.path.splitext(filepath)
file_extension_final = file_extension.replace('.', '')
try:
    #AudioSegment.converter = 'C:/Users/gragam/Desktop/ffmpeg/bin/ffmpeg.exe'
    #AudioSegment.ffmpeg = 'C:/Users/gragam/Desktop/ffmpeg/bin/ffmpeg.exe'
    #AudioSegment.ffprobe = 'C:/Users/gragam/Desktop/ffmpeg/bin/ffprobe.exe'
    track = AudioSegment.from_file(filepath)
    #wav_filename = filename.replace(file_extension_final, 'wav')
    wav_filename = 'amazon.wav'
    wav_path = 'C:/Users/gragam/Desktop/AIML/AI_Practise/AIML/SpeechSummarization/Recordings/R1/' + wav_filename
    print('CONVERTING: ' + str(filepath))
    file_handle = track.export(wav_path, format='wav')
    #os.remove(filepath)
    print("PROCESS COMPLETED")
except:
    print("ERROR CONVERTING " + str(filepath))

