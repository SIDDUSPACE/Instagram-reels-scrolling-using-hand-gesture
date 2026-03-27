# 🚀 Gesture-Based Instagram Reels Scrolling System

---

## 🎯 Overview

Control scrolling using **hand gestures** instead of touch.

This project uses real-time computer vision to track your hand and convert **index finger movement into scrolling actions**, enabling a **touchless interaction system**.

---

## 🖥️ Demo Concept

![Image](https://mediapipe.dev/images/mobile/hand_landmarks.png)

![Image](https://www.researchgate.net/publication/331135711/figure/fig7/AS%3A726713889722368%401550273501552/Scroll-control-gesture-Swipe-up-or-down-to-adjust-scroll.ppm)

![Image](https://raw.githubusercontent.com/kulin-patel/Hand-Tracking/master/Output.png)

![Image](https://miro.medium.com/1%2AFD_kpM56McFf4of2wAVuOg.jpeg)

---

## ✨ Key Features

* 🎥 Real-time webcam-based hand tracking
* ☝️ Index finger gesture recognition
* 🔄 Vertical scrolling control
* 🧠 Movement threshold filtering
* 🖼️ Live visual feedback (hand landmarks)

---

## ⚙️ Tech Stack

* **Python**
* **OpenCV** → Image processing
* **MediaPipe** → Hand tracking
* **PyAutoGUI** → System control

---

## 🧠 How It Works

![Image](https://mediapipe.dev/images/mobile/hand_landmarks.png)

![Image](https://www.xenonstack.com/hs-fs/hubfs/workflow-of-computer-vision-system.png?height=720\&name=workflow-of-computer-vision-system.png\&width=1280)

![Image](https://www.researchgate.net/publication/281643059/figure/fig1/AS%3A391423158439936%401470333961038/Flowchart-of-hand-gesture-recognition.png)

![Image](https://www.researchgate.net/publication/372073252/figure/fig5/AS%3A11431281221362926%401706758800900/Block-diagram-of-the-workflow-for-static-hand-gesture-recognition.png)

### Pipeline:

1. Capture video from webcam
2. Detect hand landmarks
3. Track index finger tip (Landmark 8)
4. Calculate vertical movement (ΔY)
5. Trigger scroll based on direction

---

## 🎮 Controls

| Gesture               | Action      |
| --------------------- | ----------- |
| Finger moves **up**   | Scroll Down |
| Finger moves **down** | Scroll Up   |
| Press `Q`             | Exit        |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/Instagram-reels-scrolling-using-hand-gesture.git
cd Instagram-reels-scrolling-using-hand-gesture
pip install opencv-python mediapipe pyautogui
```

---

## ▶️ Run the Project

```bash
python gesture_scroll.py
```

---

## ⚠️ Limitations

* Fixed threshold → not adaptive
* Sensitive to lighting conditions
* Basic gesture recognition (single gesture)
* Uses keyboard simulation instead of native scroll

---

## 🔥 Future Enhancements

* 🎯 Adaptive gesture sensitivity
* 🧠 Multi-gesture support (pinch, swipe, hold)
* ⚡ Smooth scrolling using velocity tracking
* 📱 Integration with mobile / embedded systems
* 🖥️ GUI dashboard for gesture feedback

---

## 🌍 Applications

![Image](https://www.cranksoftware.com/hubfs/Blog/2020%20Blog/crank-software-blog-the-future-of-touchless-public-touchscreens-and-GUIs_2.jpg)

![Image](https://www.mdpi.com/sensors/sensors-23-07523/article_deploy/html/images/sensors-23-07523-g001.png)

![Image](https://www.radiantvisionsystems.com/sites/default/files/styles/d06/public/images/gesture%20acquisition.png?itok=oYjiUj2n)

![Image](https://www.mdpi.com/sensors/sensors-24-03760/article_deploy/html/images/sensors-24-03760-g003-550.jpg)

* Touchless UI systems
* Accessibility tools
* Smart kiosks
* Gesture-based navigation systems

---

## 🧾 Conclusion

This project demonstrates how **computer vision + automation** can create a practical touchless interaction system. It serves as a foundation for building more advanced gesture-controlled interfaces.

---

⭐ If you found this useful, consider giving it a star!
