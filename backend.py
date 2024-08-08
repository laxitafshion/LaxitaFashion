from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
app = Flask(__name__)
CORS(app)

def search_images(search_term):
    with open('/home/laxitafashion/LAXITA/data.json', 'r') as file:
        file_names = json.load(file)
        image_paths = ['DATA/' + name for name in file_names if search_term.lower() in name.lower()]
        return image_paths

@app.route('/search')
def search():
    search_term = request.args.get('q', '')
    image_urls = search_images(search_term)
    return jsonify(image_urls)

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=7000, debug=True)
    print(search_images('gt'))