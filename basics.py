from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("/home/ritika/Documents/selenium-env/env/scrapy/scrapy_project/chromedriver",chrome_options=options)

##headless browser
# a browser which does not dispose a graphical user interface

driver.get("https://duckduckgo.com/")

# driver.find_element_by_id("search_from_input_homepage")
# driver.find_element_by_class_name()
# driver.find_element_by_tag_name("h1")
# driver.find_element_by_xpath()
# driver.find_element_by_css_selector()


##-------by xpath--------##

# search_btn=driver.find_element_by_xpath("(//input[contains(@class,'js-search-input')])[1]")
# search_btn.send_keys("My User Agent")

# search_btn=driver.find_element_by_id("search_button_homepage")
# search_btn.click()

search_input=driver.find_element_by_id("search_form_input_homepage")
search_input.send_keys("My User Agent")

search_input.send_keys(Keys.ENTER)

print(driver.page_source)

driver.close()

