import os
import argparse

from pydub import AudioSegment

formats_to_convert = ['.m4a']

filename = 'CallData.m4a'
filepath = 'C:/Users/gragam/Desktop/AIML/AI_Practise/AIML/SpeechSummarization/Recordings/R1/' + filename
(path, file_extension) = os.path.splitext(filepath)
file_extension_final = file_extension.replace('.', '')
try:
    track = AudioSegment.from_file(filepath, file_extension_final)
    wav_filename = filename.replace(file_extension_final, 'wav')
    wav_path = 'C:/Users/gragam/Desktop/AIML/AI_Practise/AIML/SpeechSummarization/Recordings/R1/' + wav_filename
    print('CONVERTING: ' + str(filepath))
    file_handle = track.export(wav_path, format='wav')
    os.remove(filepath)
except:
    print("ERROR CONVERTING " + str(filepath))
