from flask import request, jsonify
from app import app
from app.scapper.goose_scraper import scrape_url

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        url = request.json.get('url')

        if not url:
            return jsonify({'error': 'URL not provided'}), 400

        data = scrape_url(url)
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
