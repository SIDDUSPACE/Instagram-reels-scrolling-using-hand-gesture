import cv2
import mediapipe as mp
import pyautogui
import time
cap = cv2.VideoCapture(0)  
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
prev_y = 0
last_scroll_time = time.time()
cooldown = 1  
while True:
    success, img = cap.read()
    if not success:  
        print("Failed to capture image.")
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            h, w, _ = img.shape
            index_tip_y = int(handLms.landmark[8].y * h)
            if prev_y != 0:
                diff = index_tip_y - prev_y
                if abs(diff) > 40 and time.time() - last_scroll_time > cooldown:
                    if diff < 0:
                        pyautogui.press('down') 
                        print("Scroll Down")
                    else:
                        pyautogui.press('up')  
                        print("Scroll Up")
                    last_scroll_time = time.time()
            prev_y = index_tip_y
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Gesture Scroll", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
