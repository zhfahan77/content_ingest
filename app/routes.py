from flask import request, jsonify
from app import app
from app.scapper.page_scraper import scrape_url

@app.route('/scrape/page', methods=['POST'])
def scrape_page():
    try:
        url = request.json.get('url')

        if not url:
            return jsonify({'error': 'URL not provided'}), 400

        data = scrape_url(url)
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
