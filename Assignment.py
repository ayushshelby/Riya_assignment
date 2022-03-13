from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.satvacart.com/fruits-vegetables/vegetables.html")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, 'top-link-checkout').click()
expected_text = 'LOGIN OR CREATE AN ACCOUNT'
actual_text = driver.find_element(By.XPATH, "//h1[contains(text(),'Login or Create an Account')]").text
assert expected_text == actual_text, f'test failed'
driver.quit()