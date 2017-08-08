from espeak import espeak

def talk(text):
    espeak.synth(text)
