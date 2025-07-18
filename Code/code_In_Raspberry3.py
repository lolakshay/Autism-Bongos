import serial
import time
import threading
import subprocess
from tkinter import Tk, Label , PhotoImage
import os

# === CONFIG ===
serial_port = '/dev/ttyUSB0'  # Change to your Arduino port
video_start = "start.mp4"
video_left = "afterleft2.mp4"
video_right = "afterright2.mp4"

# === FORCE DISPLAY TO 5-INCH SCREEN ===
os.environ['DISPLAY'] = ':0'

# === VIDEO CONTROL ===
video_process = None

def kill_video():
    global video_process
    if video_process and video_process.poll() is None:
        video_process.terminate()
        time.sleep(0.2)

def play_video_vlc(path, loop=False):
    global video_process
    kill_video()

    loop_flag = "--loop" if loop else ""
    video_process = subprocess.Popen(
        ["cvlc", "--fullscreen", "--no-osd", loop_flag, path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

# === ESC TO EXIT ===
def on_esc(event=None):
    print("Exiting...")
    kill_video()
    root.destroy()

# === SERIAL INIT ===
try:
    ser = serial.Serial(serial_port, 9600, timeout=1)
    time.sleep(2)
except Exception as e:
    print(f"Serial Error: {e}")
    exit(1)

# === GUI FOR ESC + STATUS ===
root = Tk()
root.bind('<Escape>', on_esc)
root.attributes('-fullscreen', True)
label = Label(root, text="Bongos Active", fg="white", bg="black", font=("Arial", 24))
label.pack(expand=True)

# === STATE ===
relay1_count = 0
relay2_count = 0
video_playing = "start"

def serial_listener():
    global relay1_count, relay2_count, video_playing

    while True:
        try:
            line = ser.readline().decode().strip()
            if not line:
                continue
            print(f"Serial: {line}")

            if "left" in line:
                relay1_count = 1
                if relay1_count >=1 and video_playing != "afterleft2":
                    relay1_count = 0
                    relay2_count = 0
                    video_playing = "afterleft2"
                    play_video_vlc(video_left)

            elif "right" in line:
                relay2_count =1	
                if relay2_count >=1 and video_playing != "afterright2":
                    relay1_count = 0
                    relay2_count = 0
                    video_playing = "afterright2"
                    play_video_vlc(video_right)

        except Exception as e:
            print(f"Serial Error: {e}")
            time.sleep(1)

# === STARTUP ===
print("Starting Bongos with VLC...")
threading.Thread(target=serial_listener, daemon=True).start()
play_video_vlc(video_start, loop=True)
root.mainloop()