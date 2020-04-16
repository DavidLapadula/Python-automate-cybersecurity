import pyautogui

width, height = pyautogui.size()
x, y = pyautogui.position()

print(str(width) + " " + str(height))
print(str(x) + " " + str(y))

# pyautogui.moveTo(316, 76, duration=1.5)
pyautogui.click(316, 76)

