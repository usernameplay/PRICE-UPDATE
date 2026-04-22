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
    baseURL = "https://raw.githubusercontent.com/usernameplay/KochachanVeg/refs/heads/main/veg/"
    
    items = [
        {"id":1,"name":"Tomato","name_ml":"തക്കാളി","price":40,"image": baseURL + "tomato-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":2,"name":"Potato","name_ml":"ഉരുളക്കിഴങ്ങ്","price":22,"image": baseURL + "potato-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":3,"name":"Onion Big","name_ml":"സവാള","price":32,"image": baseURL + "onionbig-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":4,"name":"Onion Small","name_ml":"ചെറിയ ഉള്ളി","price":80,"image": baseURL + "onionsmall-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":5,"name":"Amaranth Leaves","name_ml":"ചീര","price":20,"image": baseURL + "amaranthleaves-256.png","unit":"1 bunch","updated_at":"N/A"},
        {"id":6,"name":"Amla","name_ml":"നെല്ലിക്ക","price":80,"image": baseURL + "amla-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":7,"name":"Ash Gourd","name_ml":"കുമ്പളങ്ങ","price":30,"image": baseURL + "ashgourd-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":8,"name":"Banana Flower","name_ml":"കുടപ്പൻ","price":25,"image": baseURL + "bananaflower-256.png","unit":"1 pc","updated_at":"N/A"},
        {"id":9,"name":"Beetroot","name_ml":"ബീറ്റ്റൂട്ട്","price":45,"image": baseURL + "beetroot-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":10,"name":"Bitter Gourd","name_ml":"പാവയ്ക്ക","price":60,"image": baseURL + "bittergourd-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":11,"name":"Bottle Gourd","name_ml":"ചുരയ്ക്ക","price":30,"image": baseURL + "bottlegourd-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":12,"name":"Brinjal","name_ml":"വഴുതന","price":45,"image": baseURL + "brinjal-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":13,"name":"Brinjal Big","name_ml":"വലിയ വഴുതന","price":50,"image": baseURL + "brinjalbig-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":14,"name":"Cabbage","name_ml":"കാബേജ്","price":25,"image": baseURL + "cabbage-256.png","unit":"1 pc","updated_at":"N/A"},
        {"id":15,"name":"Capsicum","name_ml":"കാപ്സിക്കം","price":80,"image": baseURL + "capsicum-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":16,"name":"Cluster Beans","name_ml":"കൊത്തമര","price":55,"image": baseURL + "clusterbeans-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":17,"name":"Coconut","name_ml":"തേങ്ങ","price":35,"image": baseURL + "coconut-256.png","unit":"1 pc","updated_at":"N/A"},
        {"id":18,"name":"Colocasia","name_ml":"ചേമ്പ്","price":60,"image": baseURL + "colocasia-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":19,"name":"Coriander Leaves","name_ml":"മല്ലിയില","price":15,"image": baseURL + "corianderleaves-256.png","unit":"1 bunch","updated_at":"N/A"},
        {"id":20,"name":"Cucumber","name_ml":"വെള്ളരിക്ക","price":35,"image": baseURL + "cucumber-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":21,"name":"Curry Leaves","name_ml":"കറിവേപ്പില","price":10,"image": baseURL + "curryleaves-256.png","unit":"1 bunch","updated_at":"N/A"},
        {"id":22,"name":"Drumsticks","name_ml":"മുരിങ്ങക്കായ","price":70,"image": baseURL + "drumsticks-256.png","unit":"250 gm","updated_at":"N/A"},
        {"id":23,"name":"Elephant Yam","name_ml":"ചേന","price":70,"image": baseURL + "elephantyam-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":24,"name":"French Beans","name_ml":"ബീൻസ്","price":60,"image": baseURL + "frenchbeans-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":25,"name":"Garlic","name_ml":"വെളുത്തുള്ളി","price":120,"image": baseURL + "garlic-256.png","unit":"250 gm","updated_at":"N/A"},
        {"id":26,"name":"Ginger","name_ml":"ഇഞ്ചി","price":100,"image": baseURL + "ginger-256.png","unit":"100 gm","updated_at":"N/A"},
        {"id":27,"name":"Green Chili","name_ml":"പച്ചമുളക്","price":80,"image": baseURL + "greenchill-256.png","unit":"250 gm","updated_at":"N/A"},
        {"id":28,"name":"Ivy Gourd","name_ml":"കോവയ്ക്ക","price":45,"image": baseURL + "ivygourd-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":29,"name":"Lemon","name_ml":"നാരങ്ങ","price":60,"image": baseURL + "lemon-256.png","unit":"1 pc","updated_at":"N/A"},
        {"id":30,"name":"Plantain","name_ml":"ഏത്തക്കായ","price":50,"image": baseURL + "plantain-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":31,"name":"Pumpkin","name_ml":"മത്തങ്ങ","price":40,"image": baseURL + "pumpkin-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":32,"name":"Snake Gourd","name_ml":"പടവലങ്ങ","price":50,"image": baseURL + "snakegourd-256.png","unit":"1 kg","updated_at":"N/A"},
        {"id":33,"name":"Sweet Potato","name_ml":"മധുരക്കിഴങ്ങ്","price":40,"image": baseURL + "sweetpotato-256.png","unit":"1 kg","updated_at":"N/A"}
    ]
    
    # 100 എണ്ണം പൂർത്തിയാക്കാൻ ബാക്കി ഐറ്റങ്ങൾ
    for i in range(34, 105):
        items.append({"id":i,"name":f"Item {i}","name_ml":f"പച്ചക്കറി {i}","price":0,"image": baseURL + "tomato-256.png","unit":"1 kg","updated_at":"N/A"})

    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(items))
    return "Setup Complete with 100+ Items!"

def handler(event, context):
    return app(event, context)
    
