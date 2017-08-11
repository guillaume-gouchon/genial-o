from picamera import PiCamera

CAMERA_WARM_UP = 2 # in seconds
LATEST_PIC_PATH = "/pics/latest.jpg"

# camera = PiCamera()
# camera.resolution = (1024, 768)

def take_picture():
    print('take picture')
    # camera.start_preview()
    # time.sleep(CAMERA_WARM_UP)
    # camera.capture(LATEST_PIC_PATH)
