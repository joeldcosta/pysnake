#Text to speech (offline)
#python -m pip install pywin32
#Program description:-
#Directly read from text without saving any mp3 file
# Create a text file text_speech.txt and type your reading material

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
file = open("text_speech.txt","r")
#print(file.read())
string = file.read()
speaker.Speak(string)
