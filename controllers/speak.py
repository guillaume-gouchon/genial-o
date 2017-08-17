import subprocess


def talk(text):
    print("speak =", text)
    command = 'espeak -s 170 -p 70 -m "' + text + '"'
    subprocess.check_output(command.split(), stderr=subprocess.PIPE).decode('UTF-8')
