import subprocess

def talk(text):
    subprocess.call(['espeak "' + text + '"'])
