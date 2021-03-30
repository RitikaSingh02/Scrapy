from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Chrome("/home/ritika/Documents/selenium-env/env/scrapy/scrapy_project/chromedriver")
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
element=""
while True:
  element = driver.find_element_by_id("bigCookie").click()
  
  # WebDriverWait(driver, 3).until( driver.find_element_by_link_text( "Got it!").click() and driver.find_elements_by_css_selector(".close:nth-child(1)").click())
  
driver.close()

  
