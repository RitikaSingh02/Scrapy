import scrapy
import logging


class CovidSpider(scrapy.Spider):
    name = 'covid'  # each spider has unique name else conflict
    allowed_domains = ['www.ourworldindata.org/coronavirus']
    # as scrapy bydefault uses http so changing to https
    start_urls = ['https://ourworldindata.org/coronavirus/']

    def parse(self, response):
        countries = response.xpath(
            "//ul[@class='covid-country-tiles']/li/a")
        title = response.xpath("//h1/text()").get()
        for c in countries:
            c_name = c.xpath(".//text()").get()
            redirect = c.xpath(".//@href").get()
            self.allowed_domains.append(redirect)

            yield scrapy.Request(url=redirect, callback=self.parse_country, meta={'country_name': c_name})

    def parse_country(self, response):
        name = response.request.meta['country_name']
        yield {
            'country_name': name
        }
        # logging.info(response.url)
# for css selectors-https://try.jsoup.org/
# for xml selectors- https://scrapinghub.github.io/xpath-playground/
