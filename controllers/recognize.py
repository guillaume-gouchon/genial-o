import see as see
import display as display
import subprocess

def guess():
    see.take_picture()
    print("guessing...")

    command = 'python ../libs/classify_image.py --num_top_predictions 1 --image_file ' + see.LATEST_PIC_PATH
    result = subprocess.check_output(command.split(), stderr=subprocess.PIPE).decode('UTF-8')
    guess = result.split(',')[0]
    probability = float(re.findall(r"[-+]?\d*\.\d+|\d+", result)[0])
    print("result =", guess, round(probability), '%')

    output = "I guess it's a " + guess + " (" + str(round(probability)) + "%)"
    display.print_text(output, 1)
    return output
