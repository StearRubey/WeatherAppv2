import pyautogui
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='chromedriver.exe')
# opens the webpage
page = driver.get("https://www.google.com/maps/d/u/0/viewer?mid=1cEAhNHqp82AXABF8qU7k6sRFI4392V0e&ll=39.86977160553247%2C-104.379495&z=10")
sleep(2) # let page load
# click the 3 vertial dots
pyautogui.click(420, 170)
# click on copy map
pyautogui.click(420, 250)
sleep(1)
# click okay


sleep(5)



