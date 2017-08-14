import subprocess

def talk(text):
    print("speak =", text)
    subprocess.call(['espeak "' + text + '"'])
