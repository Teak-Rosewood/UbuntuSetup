import roslaunch 
import time 
import rospy 

class CameraNode:

    camera1 = ["/launch/camera1.launch"]
    camera2 = ["/launch/camera2.launch"]
    camera3 = ["/launch/camera3.launch"]
    camera4 = ["/launch/camera4.launch"]

    def __init__(self, isJetson):
        if(isJetson == 1):
            self.max_cameras = 2
        else:
            self.max_cameras = 1

    def getUUID(self):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        return uuid

    def get_launch_node(self, camera_name):
        uuid = self.getUUID()
        launch = roslaunch.parent.ROSLaunchParent(uuid, camera_name)
        return launch
    
    
if __name__ == '__main__':
    rospy.init_node('camera_node')
    CameraNode()
    rospy.spin()

