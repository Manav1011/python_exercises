from vosk import Model,KaldiRecognizer
import pyaudio
import json

model=Model(r'D:\python\vosk-model-small-en-in-0.4\vosk-model-small-en-in-0.4')
recognizer=KaldiRecognizer(model,16000)


cap=pyaudio.PyAudio()
stream=cap.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
stream.start_stream()
while True:
    data=stream.read(4096)
    if len(data)==0: 
        print("Say that again!!")
    if recognizer.AcceptWaveform(data):
        text=json.loads(recognizer.Result())
        print(text['text'])
        