from django.shortcuts import render
from django.http import JsonResponse
from scrapy.crawler import CrawlerProcess
from scraper.spiders.job_spider import JobSpider

def scrape_hacker_news(request):
    if 'url' in request.GET:
        custom_url = request.GET['url']
    else:
        # Default URL if no custom URL is provided
        custom_url = "https://news.ycombinator.com/"

    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    })

    # Pass the custom URL to the spider
    process.crawl(JobSpider, start_urls=[custom_url])
    process.start()
    
    # Read the JSON file generated by Scrapy
    with open("items.json", "r") as f:
        data = f.read()
    
    # Return the scraped data as JSON response
    return JsonResponse(data, safe=False)
