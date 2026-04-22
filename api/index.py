from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import requests

app = Flask(__name__)
CORS(app)

# Upstash Details
UPSTASH_URL = "https://pleasing-hagfish-93543.upstash.io"
UPSTASH_TOKEN = "gQAAAAAAAW1nAAIgcDJjMWU5NzE2NTY0OGE0MWM4YWZhYjA5NDU1MTRhYWM2OA"
headers = {"Authorization": f"Bearer {UPSTASH_TOKEN}"}

@app.route('/api/veg', methods=['GET'])
def get_veg():
    resp = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
    res_json = resp.json()
    data = res_json.get("result")
    return jsonify(json.loads(data) if data else [])

@app.route('/api/update', methods=['POST'])
def update_price():
    update_info = request.json
    item_id = int(update_info.get('id'))
    new_price = update_info.get('price')

    # Current Data fetching
    resp = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
    all_items = json.loads(resp.json().get("result") or "[]")
    
    updated = False
    for item in all_items:
        if item['id'] == item_id:
            item['price'] = str(new_price)
            item['updated_at'] = datetime.now().strftime("%Y-%m-%d %I:%M %p")
            updated = True
            break

    if updated:
        requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(all_items))
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 404

# Aadyamayi data kayttan ulla option
@app.route('/api/setup')
def setup():
    initial_data = [
        {"id": 1, "title": "Tomato", "name_ml": "തക്കാളി", "name_en": "Tomato", "name_manglish": "Thakkali", "price": "40", "unit": "1 kg", "updated_at": "N/A", "emoji": "🍅"},
        {"id": 2, "title": "Onion", "name_ml": "സവാള", "name_en": "Onion", "name_manglish": "Savala", "price": "35", "unit": "1 kg", "updated_at": "N/A", "emoji": "🧅"},
        {"id": 3, "title": "Potato", "name_ml": "ഉരുളക്കിഴങ്ങ്", "name_en": "Potato", "name_manglish": "Urulakkizhangu", "price": "30", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥔"},
        {"id": 4, "title": "Green Chilli", "name_ml": "പച്ചമുളക്", "name_en": "Green Chilli", "name_manglish": "Pachamulaku", "price": "15", "unit": "250 gm", "updated_at": "N/A", "emoji": "🌶️"}
    ]
    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(initial_data))
    return "Setup Complete! Go to home page."

def handler(event, context):
    return app(event, context)
            
