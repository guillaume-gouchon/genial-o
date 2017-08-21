import re
import see as see
import display as display
import subprocess

def guess():
    see.take_picture()

    print("guessing...")
    result = subprocess.check_output(["python", "/app/libs/classify_image.py", "--num_top_predictions=1", "--image_file=" + see.LATEST_PIC_PATH], stderr=subprocess.PIPE).decode('UTF-8')
    split = result.split(',')
    if len(split) > 0:
        print("result =", split)
        guess = split[0]
        probability = float(re.findall(r"[-+]?\d*\.\d+|\d+", split[len(split) - 1])[0])

        output = "I guess it's a " + guess + " (" + str(round(probability)) + "%)"
    else:
        output = "I don't know what it is"

    display.clear_text()
    display.print_text(output, 1)
    return output
