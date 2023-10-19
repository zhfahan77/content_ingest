from flask import request, jsonify
import json
from app.app import app, redis_client, db
from app.lib.url_parser import remove_query_params_and_fragment, get_url_domain, get_url_path
from app.scapper.page_scraper import scrape_url
from app.scapper.pdf_scraper import scrape_pdf
from app.models.scraped_data import ScrapedData

@app.route('/scrape/page', methods=['POST'])
def scrape_page():
    try:
        url = request.json.get('url')
        reCache = request.json.get('reCache')
        reScrape = request.json.get('reScrape')
        key = remove_query_params_and_fragment(url)

        if not url:
            return jsonify({'error': 'URL not provided'}), 400

        if not reCache:
            cached_data = redis_client.get(key)
            if cached_data:
                return json.loads(cached_data)

        existing_data = db.session.query(ScrapedData).filter(
            ScrapedData.domain == get_url_domain(url),
            ScrapedData.path == get_url_path(url)
        ).one_or_none()

        if existing_data and not reScrape:
            existing_data_dict = {
                'title': existing_data.title,
                'body': existing_data.body,
                'meta_description': existing_data.metadata_json['meta_description'],
                'publish_date': str(existing_data.metadata_json['publish_date']),
                'images': existing_data.metadata_json['images']
            }
            return jsonify(existing_data_dict)

        data = scrape_url(url)

        # caching for a day
        redis_client.set(key, json.dumps(data), ex=86400)

        if not reScrape:
            new_record = ScrapedData(
                domain=get_url_domain(url),
                path=get_url_path(url),
                body=data['body'],
                title=data['title'],
                metadata_json=data
            )
            db.session.add(new_record)
            db.session.commit()
        return jsonify(data)

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

@app.route('/scrape/pdf', methods=['POST'])
def scrape_pdf_url():
    try:
        url = request.json.get('url')
        reCache = request.json.get('reCache')
        key = remove_query_params_and_fragment(url)

        if not url:
            return jsonify({'error': 'URL not provided'}), 400

        if not reCache:
            cached_data = redis_client.get(key)
            if cached_data:
                return json.loads(cached_data)

        data = scrape_pdf(url)
        # caching for a day
        redis_client.set(key, json.dumps(data), ex=86400)
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
