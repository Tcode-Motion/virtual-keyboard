<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,40:0a1a2e,80:003d5c,100:00ffff&height=220&section=header&text=Virtual%20Keyboard%20v2&fontSize=52&fontColor=00ffff&animation=fadeIn&fontAlignY=38&desc=🤖%20AR%20Hand%20Gesture%20Keyboard%20%7C%20OpenCV%20%2B%20MediaPipe%20%7C%20200%20WPM&descAlignY=60&descColor=aaaaaa&descSize=15" width="100%"/>

</div>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&pause=1000&color=00FFFF&center=true&vCenter=true&width=750&lines=🤖+AI+Hand+Gesture+Virtual+Keyboard;👁️+Powered+by+OpenCV+%2B+MediaPipe;⚡+200+WPM+Capable+—+120ms+Debounce;👻+Ghost+HUD+Mode+—+Always+On+Top;🖐️+Dual+Hand+Support+—+8+Finger+Tracking;🎯+Type+in+ANY+App+Without+Touching+Keyboard;🔮+Designed+for+the+Future+of+Spatial+Computing)](https://git.io/typing-svg)

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-AI-00ffff?style=for-the-badge&logo=google&logoColor=black)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Input-ff6b35?style=for-the-badge)
![Windows](https://img.shields.io/badge/Windows_10%2F11-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

</div>

<div align="center">

[![Star](https://img.shields.io/github/stars/Tcode-Motion/virtual-keyboard?style=for-the-badge&color=yellow)](https://github.com/Tcode-Motion/virtual-keyboard/stargazers)
[![Forks](https://img.shields.io/github/forks/Tcode-Motion/virtual-keyboard?style=for-the-badge&color=blue)](https://github.com/Tcode-Motion/virtual-keyboard/forks)
[![GitHub](https://img.shields.io/badge/GitHub-Tcode--Motion-181717?style=for-the-badge&logo=github)](https://github.com/Tcode-Motion)

</div>

---

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   Type at 200 WPM — using only your hands in mid-air.               ║
║   No physical keyboard. No desk. Just you and the camera.            ║
║                                              — Tcode-Motion ⚡        ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

---

## 🤖 About

A **high-performance, augmented reality virtual keyboard** controlled by **AI hand gestures** and mouse input. Powered by **OpenCV** and **MediaPipe**, it overlays a Ghost HUD keyboard on your screen and tracks your finger movements in real-time — letting you type in **any Windows application** without ever touching a physical keyboard.

> 🎯 *Point your finger. Tap. It types. That's it. Welcome to spatial computing.*

---

## 🚀 Key Features

| ⚡ Feature | 📖 Description |
|:---|:---|
| 👻 **Ghost HUD Mode** | Uses Windows `ctypes` API — Always on Top + No-Focus. Types into ANY app without stealing window focus |
| 🎯 **Precision Strike Typing** | AI detects a "click" from decisive downward fingertip motion — Binary-State Trigger |
| ⚡ **200 WPM Capable** | Ultra-low latency with 120ms debounce timer + high-speed tracking (`alpha=0.92`) |
| ⌨️ **Full HP Layout** | Function Row (F1-F12), Navigation cluster, full Numpad — complete keyboard |
| 🖐️ **Dual-Hand Support** | Independent tracking for all 8 fingers (Index to Pinky) across both hands |
| 🎨 **Professional HUD UI** | Semi-transparent Navy-Glass aesthetic with Electric Cyan borders + Orange status indicators |
| 🔀 **Hybrid Control** | Switch between AI Hand Gestures and Mouse Clicks instantly |
| ⏱️ **Dwell Trigger** | Hold finger over key for 0.6s → visual progress bar fills → auto-types |

---

## 🧠 Core Logic & Typing Engine

### 1. 🎯 Precision Strike — Hand Gesture Detection
Uses **Depth-Aware Dynamic Thresholding** — scales sensitivity to your hand's distance from the camera:

```python
hand_scale = dist(wrist, middle_finger_base)
tap_threshold = hand_scale * 0.08
```

> A keystroke fires if a finger moves **downward by more than 8% of the hand's size** — works consistently whether your hand is near or far from the camera.

### 2. ⏱️ Dwell Fallback Trigger
Hold a finger over any key for **0.6 seconds** → a visual progress bar fills inside the key → keystroke fires automatically. Perfect for accessibility.

### 3. 👻 Ghost Window — ctypes Magic
The HUD window is rendered **invisible to the Windows Focus Manager:**

| Flag | Effect |
|:---|:---|
| `WS_EX_NOACTIVATE` | Prevents window from stealing foreground focus when clicked |
| `WS_EX_TOPMOST` | Keeps HUD above all other applications |
| `WS_EX_APPWINDOW` | Keeps it visible in Taskbar |

---

## ⌨️ Advanced Layout & Controls

### 🎛️ Function Keys (F1-F12)

| Mode | Behaviour |
|:---:|:---|
| **Normal Mode** | Media Controls — Emoji Panel, Brightness, Volume, Mic Mute, Media Prev/Play/Next |
| **Fn-Locked Mode** | Standard Windows F1-F12 keys |

### 🔢 Dual-Mode Numpad

| Mode | Behaviour |
|:---:|:---|
| **NumLock ON** | Standard numeric entry (0-9, . , Enter) |
| **NumLock OFF** | Navigation Cluster — Home, End, PgUp, PgDn, Arrows, Insert, Delete |

### 🔘 System Buttons
- **Pwr** — Top right. Instantly closes the Virtual Keyboard
- **Shift / Ctrl / Alt** — Sticky toggles. Click once to lock, click again to release

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Camera_%26_AR-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand_Tracking-00ffff?style=for-the-badge&logo=google&logoColor=black)
![NumPy](https://img.shields.io/badge/NumPy-Math_%26_Geometry-013243?style=for-the-badge&logo=numpy&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Keystroke_Injection-ff6b35?style=for-the-badge)
![ctypes](https://img.shields.io/badge/ctypes-Ghost_HUD_Window-9b59b6?style=for-the-badge)

</div>

| Library | Purpose |
|:---|:---|
| **OpenCV** | Camera feed capture, frame rendering, AR overlay |
| **MediaPipe** | Real-time AI hand landmark detection (21 points per hand) |
| **NumPy** | Geometry math — distance calculations, thresholding |
| **PyAutoGUI** | Injects real keystrokes into active Windows applications |
| **ctypes** | Windows API — Ghost HUD window flags |

---

## 📦 Installation

### Prerequisites
- Windows 10 or 11
- Python 3.10+
- Standard webcam

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/Tcode-Motion/virtual-keyboard.git
cd virtual-keyboard

# 2. Install dependencies
pip install opencv-python mediapipe pyautogui numpy

# 3. Run the application
python virtual_keyboard_v2_main.py
```

---

## 🎮 How to Use

```
Step 1 → Run the script → Ghost HUD keyboard appears on screen
Step 2 → Position hands in front of webcam
         → Glowing MediaPipe landmarks overlay your fingers
Step 3 → Use a quick "pecking" tap motion toward camera to type
         OR simply click any key with your mouse
Step 4 → Click into any app (Notepad, Chrome, Discord, Games)
         → Virtual Keyboard injects text directly — globally
Step 5 → Exit: click Pwr button (top right) or press Q
```

---

## 📁 Project Structure

```
virtual-keyboard/
├── virtual_keyboard_v2_main.py   # Main entry point — run this
└── README.md
```

---

## 📜 System Requirements

| Requirement | Spec |
|:---|:---|
| **OS** | Windows 10 / 11 (Ghost HUD ctypes required) |
| **Python** | 3.10 or higher |
| **Hardware** | Standard webcam |
| **Dependencies** | opencv-python, mediapipe, pyautogui, numpy |

---

## 🤝 Contributing

Contributions welcome — especially for:
- 🎯 Gesture smoothing improvements
- 🎨 HUD aesthetic upgrades
- 🐧 Linux/macOS port (replacing ctypes with cross-platform alternative)

- ⭐ **Star** the repo if you like it!
- 🐛 **Open an issue** for bugs
- 🔧 **Submit a PR** for improvements

---

## 👨‍💻 Author

<div align="center">

**Tanmoy — Tcode-Motion**

[![GitHub](https://img.shields.io/badge/GitHub-Tcode--Motion-181717?style=for-the-badge&logo=github)](https://github.com/Tcode-Motion)
[![YouTube](https://img.shields.io/badge/YouTube-Sach%20Ka%20Switch-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@sachkaswitch)

*"Predict the future by coding it." ⚡*

</div>

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00ffff,50:003d5c,100:0d0d0d&height=120&section=footer&text=🔮%20Designed%20for%20Spatial%20Computing&fontSize=20&fontColor=00ffff&animation=fadeIn&fontAlignY=65" width="100%"/>

</div>
