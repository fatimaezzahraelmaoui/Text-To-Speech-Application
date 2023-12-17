from gtts import gTTs 

#data
txt = "welcome in my channel"
langue ='en'

#pass data as parameter
res = gTTs(txt=txt, lang=langue)
res.save("audio.mp3")
