import subprocess


def talk(text):
    print("speak =", text)
    subprocess.check_output(['espeak', '-s 170 -p 70 -m "' + text + '"'], stderr=subprocess.PIPE).decode('UTF-8')
