import pyautogui
while True:
    p = pyautogui.locateCenterOnScreen("C:\\Users\\rhtjd\\Documents\\Test\\LOLAutoMatchingaccept\\SuRak.png")
    if(p != None):
        pyautogui.click(p)
        print('발견')
    print('발견되지 않음')