from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# JSON ഫയലിന്റെ പാത്ത്
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/vegetables.json')

@app.route('/api/veg', methods=['GET'])
def get_veg():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

# വിസിറ്റർക്ക് കാണാൻ വേണ്ടി മാത്രം (Vercel-ൽ താൽക്കാലികമായി കാണും)
@app.route('/api/update', methods=['POST'])
def update_price():
    incoming = request.json
    # ഇവിടെ നിങ്ങൾക്ക് അപ്‌ഡേറ്റ് ലോജിക് എഴുതാം
    return jsonify({"status": "Price update received", "data": incoming})

def handler(event, context):
    return app(event, context)
  
