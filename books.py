import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["www.epubbooks.com"]
    start_urls = ["https://www.epubbooks.com/"]

    def parse(self, response):
        pass
