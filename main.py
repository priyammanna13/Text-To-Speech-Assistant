import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = input("Anything else to say:")
speak.Speak(text)


time.sleep(5)

text = "This text is read after 3 seconds"
speak.Speak(text)
