from flask import request, jsonify
import json
from app import app, redis_client
from app.scapper.page_scraper import scrape_url
from app.scapper.pdf_scraper import scrape_pdf

@app.route('/scrape/page', methods=['POST'])
def scrape_page():
    try:
        url = request.json.get('url')
        reCache = request.json.get('reCache')

        if not url:
                return jsonify({'error': 'URL not provided'}), 400

        if not reCache:
            cached_data = redis_client.get(url)
            if cached_data:
                return json.loads(cached_data)

        data = scrape_url(url)
        redis_client.set(url, json.dumps(data), ex=3600)
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/scrape/pdf', methods=['POST'])
def scrape_pdf_url():
    try:
        url = request.json.get('url')
        reCache = request.json.get('reCache')

        if not url:
            return jsonify({'error': 'URL not provided'}), 400

        if not reCache:
            cached_data = redis_client.get(url)
            if cached_data:
                return json.loads(cached_data)

        data = scrape_pdf(url)
        redis_client.set(url, json.dumps(data), ex=3600)
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
