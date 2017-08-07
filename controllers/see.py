from picamera import PiCamera

camera = PiCamera()

def startCamera():
    camera.start_preview()
    camera.start_recording('/app/video.h264')

def stopCamera():
    camera.stop_recording()
    camera.stop_preview()
