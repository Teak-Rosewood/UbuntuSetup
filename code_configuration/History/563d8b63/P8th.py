import roslaunch 
import time 
import rospy 
from std_msgs.msg import Float32MultiArray

class CameraNode:

    def __init__(self, processor):

        # Camera Launch Files

        self.camera1 = ["/launch/camera1.launch"]
        self.camera2 = ["/launch/camera2.launch"]
        self.camera3 = ["/launch/camera3.launch"]
        self.camera4 = ["/launch/camera4.launch"]

        # Camera Handeler Subscriber

        self.camera_handler = rospy.Subscribe("/camera_handler", Float32MultiArray, self.camera_handler_callback)

        # Selecting Jetson, RPi 1, Rpi 2

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

        # Checking if the device is a Jetson

        if(self.processor == 0):
            arr = [camera_data[0], camera_data[1], camera_data[2], camera_data[3]]
        
        # Checking if the device is an Raspberry Pi

        elif (self.processor == 1 or self.processor == 2):

            # Checking Raspberry Pi Number
            
            if(self.processor == 1):
                arr = [camera_data[4], camera_data[5]]
            else:
                arr = [camera_data[6], camera_data[7]]

            # Customizing Camera 1
            
            if(arr[0] == 1):
                if(self.node_arr[0] == 0):
                   launch = self.get_launch_node(self.camera1)
                   launch.start()
                   self.node_arr[0] = launch
            else:
                if(self.node_arr[0] != 0):
                    launch = self.node_arr[0] 
                    launch.shutdown()
                    self.node_arr[0] = 0

            # Customizing Camera 2

            if(arr[1] == 1):
                if(self.node_arr[1] == 0):
                   launch = self.get_launch_node(self.camera1)
                   launch.start()
                   self.node_arr[1] = launch
            else:
                if(self.node_arr[1] != 0):
                    launch = self.node_arr[0] 
                    launch.shutdown()
                    self.node_arr[1] = 0


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

