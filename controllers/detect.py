from board import raspiRobotBoard

def getFrontDistance():
    distance = raspiRobotBoard.get_distance()
    print('getFrontDistance', distance)
    return distance
