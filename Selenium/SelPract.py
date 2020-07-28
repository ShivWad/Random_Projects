from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('S:\Python/chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 1000)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = "Saishaaaaaaaa"

# Replace the below string with your own message
string = 'What up'
x = int(input())
if x == 1:
	x_arg = '//span[contains(@title,' + target + ')]'
	group_title = wait.until(EC.presence_of_element_located((
		By.XPATH, x_arg)))
	group_title.click()
	inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
	input_box = wait.until(EC.presence_of_element_located((
		By.XPATH, inp_xpath)))
	print('here')
	for i in range(100):
		print('Hi')
		input_box.send_keys(string + Keys.ENTER)

		time.sleep(1)

