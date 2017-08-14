import picamera
import time

CAMERA_WARM_UP = 2 # in seconds
LATEST_PIC_PATH = "/data/latest_picture.jpg"

def take_picture():
    print('take picture')
    with picamera.PiCamera() as camera:
        camera.resolution = (1200, 800)
        print('camera is ready, warming up...')
        time.sleep(CAMERA_WARM_UP)
        camera.capture(LATEST_PIC_PATH)
        print('picture taken')
