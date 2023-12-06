import roslaunch
import time
from queue import Queue

# Initialising queue 

q=[]
def Enqueue(element):
    q.append(element)

def Dequeue():
    e=q.pop(0)
    return e


# Defining Launch Files

camera1 = ["/launch/camera1.launch"]
camera2 = ["/launch/camera2.launch"]
camera3 = ["/launch/camera3.launch"]
camera4 = ["/launch/camera4.launch"]

# Initialising Roslaunch parameters 

def getUUID():
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    return uuid

# Making launch Nodes

def get_launch_node(camera_name):
    uuid = getUUID()
    launch = roslaunch.parent.ROSLaunchParent(uuid, camera_name)
    return launch

# front_launch.star    time.sleep(3)()
# Enqueue(mast_launch)

while (1):
    time.sleep(2)
    print("1 - mast cam")
    print("2 - front cam")
    print("3 - misc 1 cam")
    print("4 - misc 2 cam")
    num = int(input("Enter camera to add to queue: "))

    if num == 1:    
        if len(q) >= 2:

            # Dequing camera node 

            temp = Dequeue()
            print("Camera removed: ", temp)
            temp.shutdown()

            # Launching new camera 

            launch = get_launch_node(mast_cam)
            Enqueue(launch)
            launch.start()
        else:
            # Launching new camera 

            launch = get_launch_node(mast_cam)
            Enqueue(launch)
            launch.start()

    elif num == 2:
        if len(q) >= 2:

            # Dequing camera node 

            temp = Dequeue()
            print("Camera removed: ", temp)
            temp.shutdown()

            # Launching new camera 

            launch = get_launch_node(front_cam)
            Enqueue(launch)
            launch.start()
        else:
            # Launching new camera 

            launch = get_launch_node(front_cam)
            Enqueue(launch)
            launch.start()
    else:
        temp = Dequeue()
        print("Camera removed: ", temp)
        temp.shutdown()