import talkey

tts = talkey.Talkey(
    preferred_languages=["en", "fr"],
    espeak={
        "defaults": {
            "words_per_minute": 150,
            "variant": "f4",
        },
        "languages": {
            "en": {
                "voice": "english-mb-en1",
                "words_per_minute": 130
            },
        }
    }
)

def talk(text):
    tts.say(text)
