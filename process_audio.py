from pydub import AudioSegment
from pydub.utils import make_chunks
import os


def process_sudio(file_name):
    inp = "inp/" + file_name
    myaudio = AudioSegment.from_file(inp, "wav")
    chunk_length_ms = 20000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
    for i, chunk in enumerate(chunks):
        print(file_name)
        chunk_name = 'out/' + file_name + "_{0}.wav".format(i)
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")

all_file_names = os.listdir("inp")
# try:
#     os.makedirs('inp') # creating a folder named chunked
# except:
#     pass
for each_file in all_file_names:
    if ('.wav' in each_file):
        process_sudio(each_file)