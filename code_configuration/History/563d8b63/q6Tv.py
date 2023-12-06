import roslaunch 
import time 
import rospy 
from std_msgs.msg import Float32MultiArray

class CameraNode:

    camera1 = ["/launch/camera1.launch"]
    camera2 = ["/launch/camera2.launch"]
    camera3 = ["/launch/camera3.launch"]
    camera4 = ["/launch/camera4.launch"]

    def __init__(self, processor):
        self.camera_handler = rospy.Subscribe("/camera_handler", Float32MultiArray, self.camera_handler_callback)
        self.processor = processor
        if(processor == 0):
            self.rpi_number = 0
            self.max_cameras = 2
            self.node_arr = [0, 0, 0, 0]
        elif processor == 1:
            self.max_cameras = 1
            self.node_arr = [0, 0]
        else:
            self.max_cameras = 1
            self.node_arr = [0, 0]

    def camera_handler_callback(self, msg):
        camera_data = msg
        if(self.processor == 0):
            arr = [camera_data[0], camera_data[1], camera_data[2], camera_data[3]]
        elif (self.processor == 1):
            arr = [camera_data[4], camera_data[5]]
        else:
            arr = [camera_data[6], camera_data[7]]

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

