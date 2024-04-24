import scrapy

class JobSpider(scrapy.Spider):
    name = "job_spider"
    
    def __init__(self, *args, **kwargs):
        super(JobSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get('start_urls', ['https://news.ycombinator.com/'])

    def parse(self, response):
        for article in response.css("tr.athing"):
            yield {
                "title": article.css("a.storylink::text").get(),
                "url": article.css("a.storylink::attr(href)").get(),
            }
        next_page = response.css("a.morelink::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
