import random
import json
from gtts import gTTS
import os.path

b = random.randint(0, 666)
filename = './joke_mp3/' + str(b) + '.mp3'
if os.path.exists(filename):
    print(111)
else:
    f = open('jokes.json')
    data = json.load(f)
    sp = gTTS(text=data[str(b)], lang='ru', slow=False)
    sp.save(filename)
