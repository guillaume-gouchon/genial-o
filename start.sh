# enable camera
modprobe v4l2_common
python robot.py &
python server.py
