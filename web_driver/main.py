from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Aedin/Documents/ChromeDriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()

# I am a person!
options.add_argument("disable-gpu")   # Disable GPU (fast speed X)
options.add_argument("lang=ko_KR")    # psudo plugin
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')

# Move to Login Page
driver.get("https://www.kcu.ac")



driver.find_element(By.XPATH, '/html/body/header/div[1]/div[1]/div/div/h4/ul/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="contents"]/article/div/div/div/div/div[1]/ul/li[3]/a').click()

driver.find_element(By.ID, "UserID").send_keys("21111505")
driver.find_element(By.XPATH, '//*[@id="Kakao_LoginMyform"]/section/div[2]/div/label').click()
driver.find_element(By.XPATH, '//*[@id="Kakao_LoginMyform"]/section/div[3]/a').click()


#driver.close()
#driver.quit()