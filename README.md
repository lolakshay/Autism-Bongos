# 🥁 Bongos Interactive FSR Response System

A creative hardware-software interactive project that responds to physical taps using Force Sensitive Resistors (FSRs) to play dynamic videos on an LCD via a Raspberry Pi + Arduino combo.

> 🎬 Hit the bongos (FSRs), trigger a video. Designed for gamified learning, music interfaces, or AI gesture training pipelines.

---

## 🚀 Features

- 🎛️ Dual FSR sensor input (left and right taps)
- 📽️ Fullscreen video playback (start, left, right)
- 🔁 Auto-reset to default looping video after action
- 🔌 Seamless serial communication between Arduino & Raspberry Pi
- 📊 Real-time FSR tap data can be logged to Excel for later ML analysis
- 🧠 Model integration ready: Send tap metadata to any AI pipeline
- 🖥️ 800x480 LCD screen output with GUI overlay
- 🔂 Supports relays to drive 12V LED light responses

---

## 🧰 Hardware Requirements

| Component               | Description                              |
|------------------------|------------------------------------------|
| 🔌 Raspberry Pi 3      | With Raspbian OS                         |
| 🧠 Arduino Uno R3       | Reads the FSR inputs                    |
| 📟 800x480 LCD display | HDMI or GPIO based                       |
| ⚡ 12V LED Strip Light | Triggered by relay switch                |
| 🖲️ 2x FSR Sensors       | Left and Right "Bongo" input             |
| 🔁 Relay Module        | To switch LED lights based on taps       |
| 📼 Videos:             | `start.mp4`, `afterleft2.mp4`, `afterright2.mp4` |

---

## 💻 Software Stack

- Python 3 (on Raspberry Pi)
- Tkinter (GUI)
- pyserial (Serial comm)
- VLC / cvlc (Video player)
- Arduino C (for sensor reading)
- psutil (optional for clean VLC process killing)
- pandas / openpyxl (optional, for FSR logging to Excel)

---

## ⚙️ Setup Instructions

## Raspberry Pi

- Connect Arduino via USB
- Install required Python packages:
    - sudo apt-get update
    - sudo apt-get install vlc
    - pip install pyserial

# Place your videos (start.mp4, afterleft2.mp4, afterright2.mp4) in the same folder as the Python script.

# Run the script:
    - python3 bongos_code_windows.py
    - Press ESC anytime to quit the program.

# Work flow demo: 
    FSR Tap -> Arduino detects -> Sends "left"/"right"
        -> Python reads Serial -> Switches video via VLC
        -> FSR data stored (optional) → Sent to AI model

# 🙌 Contributing

- Pull requests and forks are welcome! If you’d like to improve the GUI, logging system, or hardware interaction, feel free to submit ideas or PRs.

# 📜 License

MIT License – feel free to modify, use, and share for personal and educational purposes.

# 👤 Authors

- lolakshay
- aadhur
🎓 Engineering Students | 💡 AI Enthusiast
