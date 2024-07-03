import tkinter as tk
# from tkinter import filedialog, Text
# import os
# import cv2
from PIL import Image, ImageTk
# import ctypes
# import platform
# import win32api
# import win32con

import subprocess
# from pylsl import StreamInlet, resolve_stream
# #from pywinauto import Application
import time
import socket


# Create a canvas - base structure of the GUI
root = tk.Tk()

# Define functions of what happens when clicking buttons


def startConnector():
    connector_path = r"C:\Users\User03\Documents\BrainAmpSeries-1.17.0-win64\bin\BrainAmpSeries.exe"
    connector_config_path = r"C:\Users\User03\Documents\BrainAmpSeries-1.17.0-win64\bin\config_128ch_good.cfg"
    subprocess.Popen([connector_path, "-c", connector_config_path])

def startLR():
    labrecorder_path = r"C:\Users\User03\Documents\LabRecorder\LabRecorder.exe"
    config_file_path = r"C:\Users\User03\Documents\LabRecorder\config_ue_eva.cfg"
    subprocess.Popen([labrecorder_path, "-c", config_file_path])

def startViewer():
    viewer_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\BrainVision\BrainVision LSL Viewer.lnk"
    subprocess.Popen(viewer_path, shell=True)

def startAll():
    # time.sleep(5)
    startConnector()
    startLR()
    startViewer()
    startRecord.config(state=tk.NORMAL)
    # Call the Polar2LSL.py script
    subprocess.call(["python", "Polar2LSL.py"])

# Define function to send subject number
def submit_subjectNumber():
    subjectNumber = entry.get()
    print('Submitted text:', subjectNumber)
    return subjectNumber

def startRecording():
    subjectNumber = submit_subjectNumber()
    subjectNumber_bytes = subjectNumber.encode("utf-8")

    ## Get subject number to name the created folder
    # s = socket.create_connection(("localhost", 22345))
    s = socket.create_connection(("localhost", 7000))
    s.sendall(b"select all\n")  # see if in the eeg room other streams are there, otherwise it does not matter


    s.sendall(b"filename {C:\Users\experimentPC310\Documents\Eva\DATA} {template:exp%n\\%p_block_%b.xdf}"
              b"{run:} {participant:" + subjectNumber_bytes + b"}{task:}\n")
    # s.sendall(b"filename {C:\Users\User03\Documents\CurrentStudy\testFolder} {template:exp%n\\%p_block_%b.xdf}"
    #           b"{run:} {participant:" + subjectNumber_bytes + b"}{task:MemoryGuided}\n")
    s.sendall(b"start\n")

#
# Prepare camera
# Define the desired width and height for the display
DISPLAY_WIDTH = 512 #320 #640
DISPLAY_HEIGHT = 384 #240 #480

# def update_frame():
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.resize(frame, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(frame)
#         photo = ImageTk.PhotoImage(image)
#         label.config(image=photo)
#         label.image = photo
#     # Call this function again after a delay
#     label.after(10, update_frame)


# Canvas - background of the GUI
canvas = tk.Canvas(root, height=1600, width=800, bg='#011330')
canvas.pack()

frame = tk.Frame(root, bg='#f7b0db')
frame.pack()
frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)


# Create the dialog box
dialogBox = tk.Text(root, height=5, width=30)
dialogBox.insert(tk.END, 'Hello world!')
dialogBox.pack()
dialogBox.place(relx=0.1, rely=0.7)

# Create field to fill in subject number
label = tk.Label(root, text="Enter subject number:")
label.place(relx=0.1, rely=0.1)

entry = tk.Entry(root)
entry.place(relx=0.1, rely=0.15)

button = tk.Button(root, text="Submit", command=submit_subjectNumber)
button.place(relx=0.1, rely=0.2)


# Add button to launch UE and following apps
startApps = tk.Button(root, text='Launch UE', padx=10, pady=5, fg='white', bg='#011330', command=startAll)
#startApps.pack()
startApps.place(relx=0.1, rely=0.3)


# Add button to start recording
startRecord = tk.Button(root, text='Start Recording', padx=10, pady=5, fg='white', bg='#011330', command=startRecording)
startRecord.config(state=tk.DISABLED)  # Disable the button
#startRecord.pack()
startRecord.place(relx=0.1, rely=0.4)






# # Add camera
# # Open the camera
# cap = cv2.VideoCapture(0)  # Use 0 for default camera or specify the camera index
#
# # Create a label to display the video feed
# label = tk.Label(root)
# label.pack()
# label.place(relx=0.1, rely=0.5)
#
#
# # Start capturing and updating the frames
# update_frame()
#
#
# Open GUI
root.mainloop()

# # Release the camera and cleanup
# cap.release()



