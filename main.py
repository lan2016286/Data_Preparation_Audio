# This is a sample Python script.
from pydub import AudioSegment
from pydub.utils import make_chunks
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def convert_mp3_to_wav(inp):
    inp = "inp/" + inp
    inp_mp3 = inp.split("/")
    out_wav = "output_wav/" + inp_mp3[-1][:-3] + 'wav'
    script_convert_mp3_wav = "ffmpeg -i " + inp + ' ' + out_wav
    os.system(script_convert_mp3_wav)
    out_wav_16k = "output_wav_16k/" + out_wav.split("/")[-1]
    script_convert_sampling_rate = "ffmpeg -i " + out_wav + " -ar 16000 " + out_wav_16k
    return os.system(script_convert_sampling_rate)


def process_sudio(file_name):
    inp = "output_wav_16k/" + file_name
    myaudio = AudioSegment.from_file(inp, "wav")
    chunk_length_ms = 20000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
    for i, chunk in enumerate(chunks):
        print(file_name)
        chunk_name = 'out/' + file_name + "_{0}.wav".format(i)
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    files = os.listdir("inp")
    for each_file in files:
        convert_mp3_to_wav(each_file)
    all_file_names = os.listdir("output_wav_16k")
    for each_file in all_file_names:
        if ('.wav' in each_file):
            process_sudio(each_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
