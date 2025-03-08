import speech_recognition as sr
# obtain audio from the microphone
def speach():
    r = sr.Recognizer()
    with sr.Microphone(2) as source:
        print("Sir, say something")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Sir, this is what you said - " + r.recognize_google(audio))
speach()
