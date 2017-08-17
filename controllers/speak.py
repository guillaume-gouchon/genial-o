import subprocess


def talk(text):
    print("speak =", text)
    subprocess.check_output(["espeak", text, "-s 170", "-p 70"], stderr=subprocess.PIPE).decode('UTF-8')
