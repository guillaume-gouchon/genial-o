import subprocess

def talk(text):
    subprocess.call(['espeak "' + text + '" 2>/dev/null'])
