# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFirst():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_first(self):
    self.driver.get("https://www.spotify.com/in/")
    self.driver.set_window_size(1366, 734)
    self.driver.execute_script("window.scrollTo(0,244)")
    self.driver.find_element(By.ID, "segmented-desktop-launch").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.LINK_TEXT, "Search").click()
    element = self.driver.find_element(By.LINK_TEXT, "Recent searches")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_748c0c69da51ad6d4fc04c047806cd4d-scss").send_keys("bts")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_748c0c69da51ad6d4fc04c047806cd4d-scss").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".\\_85fec37a645444db871abd5d31db7315-scss").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_95e9f2bdf9c64702a6123c2d6de8076b-scss polygon").click()
  
