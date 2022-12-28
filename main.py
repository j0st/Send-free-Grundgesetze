import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


url = 'https://www.bpb.de/shop/buecher/grundgesetz/34367/grundgesetz-fuer-die-bundesrepublik-deutschland/'

amount = 6
first_name = 'Test'
last_name = 'Test'
street = 'Teststr.' 
street_number = '1'
postal_code = '11111'
city = 'Test'
email = 'test@fyii.de'

# start page
driver.get(url)
driver.find_element(By.XPATH, '/html/body/div/main/article/div/div[2]/section[1]/section/form/div/div[1]/div/input').send_keys(Keys.BACKSPACE)
driver.find_element(By.XPATH, '/html/body/div/main/article/div/div[2]/section[1]/section/form/div/div[1]/div/input').send_keys(amount)
driver.find_element(By.XPATH, '//*[@id="app"]/main/article/div/div[2]/section[1]/section/form/div/div[2]/button').click()
time.sleep(5)

# added to cart page
driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div/article/footer/a').click()
time.sleep(5)

# to checkout
driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/form/div/div[2]/button').click()
time.sleep(5)

# adress page
driver.find_element(By.XPATH, '/html/body/div/main/div[6]/div[2]/div/form/div[2]/fieldset/div/div[1]/div/input').send_keys(first_name)
driver.find_element(By.XPATH, '/html/body/div/main/div[6]/div[2]/div/form/div[2]/fieldset/div/div[2]/div/input').send_keys(last_name)
driver.find_element(By.XPATH, '/html/body/div/main/div[6]/div[2]/div/form/div[2]/fieldset/div/div[4]/div/input').send_keys(street)
driver.find_element(By.XPATH, '/html/body/div/main/div[6]/div[2]/div/form/div[2]/fieldset/div/div[5]/div/input').send_keys(street_number)
driver.find_element(By.XPATH, '/html/body/div/main/div[6]/div[2]/div/form/div[2]/fieldset/div/div[6]/div/input').send_keys(postal_code)
driver.find_element(By.XPATH, '/html/body/div/main/div[6]/div[2]/div/form/div[2]/fieldset/div/div[7]/div/input').send_keys(city)
driver.find_element(By.XPATH, '/html/body/div/main/div[6]/div[2]/div/form/div[2]/fieldset/div/div[9]/div/input').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="app"]/main/div[6]/div[2]/div/form/div[3]/button').click()

# submit page
driver.find_element(By.XPATH, '//*[@id="app"]/main/form/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/label').click()
driver.find_element(By.XPATH, '//*[@id="app"]/main/form/div[2]/div[2]/div/div[2]/div[3]/div/div[3]/div/label').click()
#driver.find_element(By.XPATH, '//*[@id="submit-shop-order"]/button').click()
print('passed')
time.sleep(10)

driver.quit()