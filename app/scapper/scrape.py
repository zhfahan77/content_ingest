from app.lib.url_parser import get_url_extension
from app.scapper.page_scraper import scrape_page
from app.scapper.pdf_scraper import scrape_pdf

def scrape(url):
    ext = get_url_extension(url)

    if ext == '.pdf':
        data = scrape_pdf(url)
        return data
    elif not ext:
        data = scrape_pdf(url)
        return scrape_page(url)