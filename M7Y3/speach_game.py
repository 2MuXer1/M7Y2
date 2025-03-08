import speech_recognition as speech_recog

def speach():
    mic = speech_recog.Microphone(2)
    recog = speech_recog.Recognizer()
    with mic as source:
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)
        return recog.recognize_google(audio)
