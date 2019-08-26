import math
import os
import random
import re
import sys
import speech_recognition as sr


if __name__ == '__main__':
    r = sr.Recognizer()

    with sr.AudioFile('./Recordings/R1/def.wav') as source:
        audio = r.record(source)

    response = r.recognize_google(audio)
    print(response)

