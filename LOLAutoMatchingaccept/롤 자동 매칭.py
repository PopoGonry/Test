import pyautogui
while True:
    p = pyautogui.locateCenterOnScreen("C:\\Users\\rhtjd\\Desktop\\SuRak.png")
    if(p != None):
        pyautogui.click(p)
        print('발견')
        break
    print('발견되지 않음')