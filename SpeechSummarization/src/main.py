# importing libraries
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# a function that splits the audio file into chunks
# and applies speech recognition


def silence_based_conversion(path):
    # open the audio file stored in the local system as a wav file.
    audio = AudioSegment.from_wav(path)

    # open a file where we will concatenate
    # and store the recognized text
    fh = open("recognized.txt", "w+")
    # considering silence in decibles(dBFS)
    #, min_silence_len=100, silence_thresh=-16
    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-60)
    print(chunks)
    # create a directory to store the audio chunks.
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass

    # move into the directory to
    # store the audio files.
    os.chdir('audio_chunks')

    i = 0
    # process each chunk
    for chunk in chunks:
        # Create 0.5 seconds silence chunk
        chunk_silent = AudioSegment.silent(duration=100)
        print('Added Silence')
        # add 0.5 sec silence to beginning and
        # end of audio chunk. This is done so that
        # it doesn't seem abruptly sliced.
        audio_chunk = chunk_silent + chunk + chunk_silent

        # export audio chunk and save it in
        # the current directory.
        print("saving chunk{0}.wav".format(i))
        # specify the bitrate to be 192 k
        audio_chunk.export("./chunk{0}.wav".format(i),
                        bitrate='192k', format="wav")

        # the name of the newly created chunk
        filename = 'chunk'+str(i)+'.wav'

        print("Processing chunk "+str(i))

        # get the name of the newly created chunk
        # in the AUDIO_FILE variable for later use.
        file = filename

        # create a speech recognition object
        r = sr.Recognizer()

        # recognize the chunk
        with sr.AudioFile(file) as source:
                # remove this if it is not working
                # correctly.
                r.adjust_for_ambient_noise(source)
                audio_listened = r.record(source)

        try:
            # try converting it to text
            rec = r.recognize_ibm(audio_listened)
            # write the output to the file.
            fh.write(rec+". ")

        # catch any errors.
        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Could not request results. check your internet connection")
        i += 1
    os.chdir('..')
    
if __name__ == '__main__':
    path = './Recordings/R1/amazon.wav'
    silence_based_conversion(path)
