from picamera import PiCamera

CAMERA_WARM_UP = 2 # in seconds
LATEST_PIC_PATH = "latest_picture.jpg"

camera = PiCamera()
camera.resolution = (1024, 768)

def take_picture():
    print('take picture')
    camera.capture(LATEST_PIC_PATH)
    print('3')
