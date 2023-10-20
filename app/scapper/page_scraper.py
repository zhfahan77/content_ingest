from goose3 import Goose
from bs4 import BeautifulSoup

def get_images(images_tags):
    image_urls = []
    for image in images_tags:
        if(image.get('src')) and image.get('width'):
            image_urls.append(image.get('src'))
    return image_urls

def scrape_page(url):
    g = Goose({ 'browser_user_agent': 'Mozilla', 'parser_class':'soup' })
    article = g.extract(url=url)

    soup = BeautifulSoup(article.raw_html, 'html.parser')
    img_tags = soup.find_all('img')
    image_urls = get_images(img_tags)

    data = {
        'title': article.title,
        'body': article.cleaned_text,
        'meta_description': article.meta_description,
        'publish_date': str(article.publish_date),
        'images': image_urls
    }

    return data