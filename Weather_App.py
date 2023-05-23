import requests
import json
import pyttsx3

city=input("Enter the name of city\n")
url=f"https://api.weatherapi.com/v1/current.json?key=d2243ad759ae496e9d3120454232305&q={city}"
r=requests.get(url)
Wdic=json.loads(r.text)
W=Wdic["current"]["temp_c"]

engine=pyttsx3.init()
engine.say(f"The current weather in {city} is {W} degrees")
engine.runAndWait()