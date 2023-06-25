import pyautogui
import time

# 1. 화면 크기 출력
print(pyautogui.size())

# 2. 마우스 위치 출력
time.sleep(2)
print(pyautogui.position())

# 3. 마우스 이동

# 한 번에 이동
# pyautogui.moveTo(300, 200)

# a초 만큼 이동
pyautogui.moveTo(389, 19, 2)

# 4. 마우스 클릭
pyautogui.click()
pyautogui.doubleClick()
pyautogui.click(button='right')
pyautogui.click(clicks=3, interval=1) # 3번 클릭 1초마다

# 5. 마우스 드래그
# 477,50 -> 670,54
pyautogui.moveTo(477,50,2)
pyautogui.dragTo(670,54,2)