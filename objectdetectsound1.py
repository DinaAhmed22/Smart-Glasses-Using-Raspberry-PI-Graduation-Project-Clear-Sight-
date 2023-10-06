import cv2
import numpy as np
import pyttsx3

#This is to pull the information about what each object is called
classNames = []

classFile ="C:\Users\Cairo\Documents\Smart_Glass_For_Blind_People\Codes and Algorithnms\Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
  classNames = f.read().rstrip("\n").split("\n")

#This is to pull the information about what each object should look like
configPath="C:\Users\Cairo\Documents\Smart_Glass_For_Blind_People\Codes and Algorithnms\Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath="C:\Users\Cairo\Documents\Smart_Glass_For_Blind_People\Codes and Algorithnms\Object_Detection_Files/frozen_inference_graph.pb"

#This is some set up values to get good results
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


# Define colors for bounding boxes and text
#colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Define function to detect objects and generate output
def detect_objects(frame):
    # Create blob from input image and pass it through the network
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    #net.setInput(blob)
    #detections = net.forward()

    # Loop over the detections and draw bounding boxes
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            x1, y1, x2, y2 = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            color = colors[class_id]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            cv2.putText(frame, classes[class_id], (int(x1), int(y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Generate audio output
            engine.say(classes[class_id])
            engine.runAndWait()

    # Display the resulting frame
    cv2.imshow('Object Detection', frame)
    cv2.waitKey(1)

# Initialize video capture object
cap = cv2.VideoCapture(0)

# Loop over frames and call detect_objects function
while True:
    ret, frame = cap.read()
    detect_objects(frame)

# Release video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
