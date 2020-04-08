import pyautogui

#print(pyautogui.position())

#pyautogui.moveTo(1000, 500)
#pyautogui.click(1832, 43)

num7 = pyautogui.locateCenterOnScreen("C:\\Users\\rhtjd\\Documents\\Test\\7.png")
if(num7 == None):
    print("논")
elif(num7 != None):
    pyautogui.click(num7)