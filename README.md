# Virtual Keyboard v2

A high-performance, augmented reality virtual keyboard controlled by AI hand gestures and mouse input. Designed with a sleek HUD aesthetic, this tool allows for seamless, global typing across all Windows applications without ever touching a physical keyboard.

![License](https://img.shields.io/badge/License-MIT-orange.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Mediapipe](https://img.shields.io/badge/AI-Mediapipe-cyan.svg)

## 🚀 Key Features

*   **Ghost HUD Mode:** Using Windows `ctypes` API, the keyboard remains **Always on Top** and **No-Focus**. It types directly into any active application (Notepad, Chrome, Games) without stealing window focus.
*   **Precision Strike Typing:** A custom AI logic that detects a "click" based on a decisive downward fingertip motion (Binary-State Trigger).
*   **200 WPM Capable:** Ultra-low latency engine with a 120ms debounce timer and high-speed finger tracking (`alpha=0.92`).
*   **Full HP Layout:** Complete keyboard including Function Row (F1-F12), Navigation cluster, and a full Numpad.
*   **Dual-Hand Support:** Independent tracking for all 8 fingers (Index to Pinky) across both hands.
*   **Professional HUD UI:** Semi-transparent Navy-Glass aesthetic with Electric Cyan borders and bright Orange status indicators.
*   **Hybrid Control:** Switch between AI Hand Gestures and Mouse Clicks instantly.

---

## 🧠 Core Logic & Typing Engine

### 1. Precision Strike (Hand Gestures)
The system uses **Depth-Aware Dynamic Thresholding**. It calculates the scale of the hand relative to the camera:
```python
hand_scale = dist(wrist, middle_finger_base)
tap_threshold = hand_scale * 0.08
```
A keystroke is triggered if a finger moves downward by more than 8% of the hand's size. This ensures sensitivity is consistent whether your hand is close to the camera or far away.

### 2. Dwell Fallback
If you hold a finger over a key for **0.6 seconds**, a "Dwell Trigger" occurs. A visual progress bar fills inside the key to indicate the countdown.

### 3. Ghost Window Styling
The window is rendered "invisible" to the Windows Focus Manager:
*   `WS_EX_NOACTIVATE`: Prevents the window from becoming the foreground window when clicked.
*   `WS_EX_TOPMOST`: Keeps the HUD above all other applications.
*   `WS_EX_APPWINDOW`: Ensures it remains visible in the Taskbar.

---

## ⌨️ Advanced Layout & Controls

### Function Keys (F1-F12)
*   **Normal Mode:** Media Controls (Emoji Panel, Brightness, Volume, Mic Mute, Media Prev/Play/Next, OMEN Gaming Hub).
*   **Fn-Locked Mode:** Acts as standard Windows F1-F12 keys.

### Dual-Mode Numpad
*   **NumLock ON:** Standard numeric entry.
*   **NumLock OFF:** Navigation Cluster (Home, End, PgUp, PgDn, Arrow Keys, Insert, Delete).

### System Buttons
*   **Pwr (Power):** Located at the top right. Instantly shuts down the Virtual Keyboard application.
*   **Shift/Ctrl/Alt:** "Sticky" toggles. Click once to lock, click again to release.

---

## 🛠️ Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Tcode-Motion/virtual-keyboard.git
    cd virtual-keyboard
    ```

2.  **Install Dependencies:**
    ```bash
    pip install opencv-python mediapipe pyautogui numpy
    ```

3.  **Run the Application:**
    ```bash
    python virtual_keyboard_v2_main.py
    ```

---

## 🎮 How to Use

1.  **Hand Positioning:** Place your hands in view of the camera. The HUD will overlay your fingers with glowing landmarks.
2.  **Typing:** Use a quick "pecking" or "tapping" motion toward the camera to type. 
3.  **Mouse:** You can also simply click any key on the HUD with your mouse.
4.  **Global Input:** Open Notepad or any chat app. Click into the app once, then start typing on the Virtual Keyboard. It will inject text directly into your app.
5.  **Exit:** Click the **Pwr** button on the top right or press `q` on your physical keyboard.

---

## 📜 Requirements
*   **OS:** Windows 10/11 (Required for Ghost HUD `ctypes` logic).
*   **Hardware:** Standard Webcam.
*   **Python:** 3.10 or higher.

## 🤝 Contributing
Feel free to fork this project and submit PRs. Technical improvements to the gesture smoothing or HUD aesthetics are always welcome!

---
*Designed for the future of spatial computing.*

