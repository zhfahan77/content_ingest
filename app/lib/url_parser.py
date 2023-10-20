from urllib.parse import urlsplit, urlunsplit, urlparse
from os.path import splitext;
def remove_query_params_and_fragment(url):
    return urlunsplit(urlsplit(url)._replace(query="", fragment=""))

def get_url_domain(url):
    return urlparse(url).netloc

def get_url_path(url):
    return urlparse(url).path

def get_url_extension(url):
    path = get_url_path(url)
    ext = splitext(path)[1]
    return ext
