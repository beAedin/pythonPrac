from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_driver_path = "C:/Users/Aedin/Documents/ChromeDriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()

# I am a person!
options.add_argument("disable-gpu")   # Disable GPU (fast speed X)
options.add_argument("lang=ko_KR")    # psudo plugin
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')

# Move to Login Page
driver.get("https://www.kcu.ac")