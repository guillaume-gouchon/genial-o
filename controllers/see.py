import picamera
import time
from camera_pi import Camera

CAMERA_WARM_UP = 2 # in seconds
LATEST_PIC_PATH = "/data/latest_picture.jpg"

def take_picture():
    print('take picture')
    if 'pi_camera' in locals():
        pi_camera.stop()
        time.sleep(0.5)

    with picamera.PiCamera() as camera:
        camera.rotation = 180
        camera.resolution = (1200, 800)
        print('camera is ready, warming up...')
        time.sleep(CAMERA_WARM_UP)
        camera.capture(LATEST_PIC_PATH)
        print('picture taken')
        generate_frames()

def generate_frames():
    pi_camera = Camera()
    while True:
        frame = pi_camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
