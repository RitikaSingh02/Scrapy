import scrapy
from selenium import webdriver
from scrapy.selector import Selector

##test
class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ["www.livecoinwatch.com"]
    start_urls = ["https://www.livecoinwatch.com/"]

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(
            "/home/ritika/Documents/selenium-env/env/scrapy/scrapy_project/chromedriver", options=options)
        driver.get("https://www.livecoinwatch.com/price/Litecoin-LTC")

        # search_input = driver.find_element_by_xpath(
        #     "(//input[@class='form-control main-small-search'][1])")
        # search_input.send_keys("LTC")

        self.html = driver.page_source
        # print(self.html)
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for search in resp.xpath("(//*[@id='__next']/div/div[1]/main/div/div[6]/div/div[2]/div/div/section/div[2]/div[1]/table/tbody/tr)"):
            yield{
                'response': "LTC",
                'search': search.xpath("./td[2]/div/div/a/text()").get()
            }
