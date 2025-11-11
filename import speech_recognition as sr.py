import speech_recognition as sr

r = sr.Recognizer()

print("Say something... (you have 15 seconds)")

try:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  
        print("Listening...")
        audio_data = r.listen(source)
        print("Processing...")
    
    text = r.recognize_google(audio_data,language="hi-IN")
    print("You said:", text)

except sr.WaitTimeoutError:
    print("No speech detected in given time.")
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError as e:
    print(f"Error with the request to Google Speech Recognition service: {e}")
except Exception as e:
    print(f"Error: {e}")