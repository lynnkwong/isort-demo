# Run the spider with the internal API of Scrapy:
from scraping_proj.spiders.authors import AuthorSpider
from scraping_proj.spiders.quotes import QuoteSpider
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


settings = get_project_settings()
process = CrawlerProcess(settings)

author_crawler = Crawler(
    AuthorSpider,
    settings={**settings, "FEEDS": {"authors.json": {"format": "json"},},},
)
quote_crawler = Crawler(
    QuoteSpider,
    settings={**settings, "FEEDS": {"quotes.json": {"format": "json"},},},
)

process.crawl(author_crawler)
process.crawl(quote_crawler, tag="love")

process.start()
