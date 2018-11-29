# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import speechKey as sk

def speechToText():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Adjusting mic...")
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, key=sk.KEY)
        print("Google Speech Recognition thinks you said {}".format(text))
        return(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return("")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return("")



