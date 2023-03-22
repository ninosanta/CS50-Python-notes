import cowsay
import pyttsx3  # Python Text to Speech library
from this import say

engine = pyttsx3.init()
this = say()
cowsay.cow(this)
engine.say(this)
engine.runAndWait()  # in case it is a long text