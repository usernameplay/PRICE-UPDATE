from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import requests
import pytz

app = Flask(__name__)
CORS(app)

UPSTASH_URL = "https://pleasing-hagfish-93543.upstash.io"
UPSTASH_TOKEN = "gQAAAAAAAW1nAAIgcDJjMWU5NzE2NTY0OGE0MWM4YWZhYjA5NDU1MTRhYWM2OA"
headers = {"Authorization": f"Bearer {UPSTASH_TOKEN}"}

def get_ist_time():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).strftime("%d-%m-%Y %I:%M %p")

@app.route('/api/veg', methods=['GET'])
def get_veg():
    try:
        resp = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
        res_data = resp.json().get("result")
        return jsonify(json.loads(res_data) if res_data else [])
    except:
        return jsonify([])

@app.route('/api/add', methods=['POST'])
def add_item():
    new_item = request.json
    resp = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
    all_items = json.loads(resp.json().get("result") or "[]")
    
    new_item['id'] = max([i['id'] for i in all_items]) + 1 if all_items else 1
    new_item['updated_at'] = get_ist_time()
    
    all_items.append(new_item)
    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(all_items))
    return jsonify({"status": "success"})

@app.route('/api/update', methods=['POST'])
def update_price():
    data = request.json
    item_id = int(data.get('id'))
    new_price = data.get('price')

    resp = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
    all_items = json.loads(resp.json().get("result") or "[]")
    
    for item in all_items:
        if item['id'] == item_id:
            item['price'] = str(new_price)
            item['updated_at'] = get_ist_time()
            break

    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(all_items))
    return jsonify({"status": "success"})

@app.route('/api/setup')
def setup():
    base = "https://raw.githubusercontent.com/usernameplay/KochachanVeg/refs/heads/main/veg/"
    items = [
        {"id":1,"name":"Tomato","name_ml":"തക്കാളി","price":"40","image": base + "tomato-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":2,"name":"Potato","name_ml":"ഉരുളക്കിഴങ്ങ്","price":"22","image": base + "potato-256.png","unit":"1 kg","updated_at":"N/A"}
    ]
    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(items))
    return "Setup Success!"
    
