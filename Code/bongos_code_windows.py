import serial
import time
import cv2
from tkinter import Tk, Label
from PIL import Image, ImageTk
import threading
import os

# === CONFIG ===
serial_port = 'COM4'  # Change if needed
video_start = "start.mp4"
video_left = "afterleft.mp4"
video_right = "afterright.mp4"

# === FORCE DISPLAY TO 5-INCH SCREEN ===
# Find your 5-inch screen's display ID (usually :0 or :1)
os.environ['DISPLAY'] = ':0'  # Try :0, :1, etc. if this doesn't work

def on_esc(event=None):
    global stop_video_flag
    print("Exiting on ESC...")
    stop_video_flag = True
    root.destroy()


# === SERIAL ===
try:
    ser = serial.Serial(serial_port, 9600, timeout=1)
    time.sleep(2)
except Exception as e:
    print(f"Serial Error: {e}")
    exit(1)

# === GUI SETUP (FULLSCREEN ON 5-INCH) ===
root = Tk()
root.bind('<Escape>', on_esc)
root.title("Bongos")
root.configure(bg="black")
root.attributes('-fullscreen', True)  # Forces fullscreen on target display

# Get screen dimensions (should match your 5-inch screen)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(f"Screen Detected: {screen_width}x{screen_height}")

label = Label(root, bg="black")
label.pack(fill="both", expand=True)

# === STATE VARIABLES ===
current_video = None
stop_video_flag = False
relay1_count = 0
relay2_count = 0
video_playing = "start"

def play_video(path, loop=False):
    global current_video, stop_video_flag, video_playing
    
    stop_video_flag = True  # Stop previous video
    time.sleep(0.1)
    
    stop_video_flag = False
    video_playing = path.split(".")[0]
    
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print(f"Failed to open: {path}")
        return
    
    while cap.isOpened() and not stop_video_flag:
        ret, frame = cap.read()
        if not ret:
            if loop:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            break
        
        frame = cv2.resize(frame, (screen_width, screen_height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(frame))

        label.config(image=img)
        label.image = img
        root.update_idletasks()
        root.update()
        
        time.sleep(0.03)
    
    cap.release()

def serial_listener():
    global relay1_count, relay2_count, video_playing
    
    while True:
        try:
            line = ser.readline().decode().strip()
            if not line:
                continue
            print(f"Serial: {line}")

            if "left" in line:
                relay1_count += 1
                print(f"RELAY1 count: {relay1_count}")
                if relay1_count >= 2 and video_playing != "afterleft":
                    relay1_count = 0
                    relay2_count = 0
                    threading.Thread(target=play_video, args=(video_left, False)).start()

            elif "right" in line:
                relay2_count += 1
                print(f"RELAY2 count: {relay2_count}")
                if relay2_count >= 2 and video_playing != "afterright":
                    relay1_count = 0
                    relay2_count = 0
                    threading.Thread(target=play_video, args=(video_right, False)).start()

        except Exception as e:
            print(f"Serial Error: {e}")
            time.sleep(1)

# === STARTUP ===
print("Starting Bongos...")
threading.Thread(target=serial_listener, daemon=True).start()
play_video(video_start, loop=True)  # Start with looping intro
root.mainloop()