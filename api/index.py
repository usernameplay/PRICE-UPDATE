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
headers = {"Authorization": f"Bearer {UPSTASH_TOKEN}", "Content-Type": "application/json"}

def get_now():
    return datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d %b, %I:%M %p")

@app.route('/api/veg', methods=['GET'])
def fetch_all():
    try:
        r = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
        data = r.json().get("result")
        return jsonify(json.loads(data) if data else [])
    except:
        return jsonify([])

@app.route('/api/save-all', methods=['POST'])
def save_all():
    # മുഴുവൻ ലിസ്റ്റും എഡിറ്റ് ചെയ്ത ശേഷം സേവ് ചെയ്യാൻ
    items = request.json
    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(items))
    return jsonify({"status": "success"})

@app.route('/api/setup')
def setup():
    # നിങ്ങൾ തന്ന പുതിയ ലിങ്ക്
    baseURL = "https://raw.githubusercontent.com/usernameplay/PRICE-UPDATE/refs/heads/main/vegimg/"
    
    items = [
        {"id":1,"name":"Tomato","name_ml":"തക്കാളി","price":40,"image": baseURL + "tomato-256.png","unit":"1 kg"},
        {"id":2,"name":"Potato","name_ml":"ഉരുളക്കിഴങ്ങ്","price":22,"image": baseURL + "potato-256.png","unit":"1 kg"},
        {"id":3,"name":"Onion Big","name_ml":"സവാള","price":32,"image": baseURL + "onionbig-256.png","unit":"1 kg"},
        {"id":4,"name":"Onion Small","name_ml":"ചെറിയ ഉള്ളി","price":80,"image": baseURL + "onionsmall-256.png","unit":"1 kg"},
        {"id":5,"name":"Amaranth Leaves","name_ml":"ചീര","price":20,"image": baseURL + "amaranthleaves-256.png","unit":"1 bunch"},
        {"id":6,"name":"Amla","name_ml":"നെല്ലിക്ക","price":80,"image": baseURL + "amla-256.png","unit":"1 kg"},
        {"id":7,"name":"Ash Gourd","name_ml":"കുമ്പളങ്ങ","price":30,"image": baseURL + "ashgourd-256.png","unit":"1 kg"},
        {"id":8,"name":"Banana Flower","name_ml":"കുടപ്പൻ","price":25,"image": baseURL + "bananaflower-256.png","unit":"1 pc"},
        {"id":9,"name":"Beetroot","name_ml":"ബീറ്റ്റൂട്ട്","price":45,"image": baseURL + "beetroot-256.png","unit":"1 kg"},
        {"id":10,"name":"Bitter Gourd","name_ml":"പാവയ്ക്ക","price":60,"image": baseURL + "bittergourd-256.png","unit":"1 kg"},
        {"id":11,"name":"Bottle Gourd","name_ml":"ചുരയ്ക്ക","price":30,"image": baseURL + "bottlegourd-256.png","unit":"1 kg"},
        {"id":12,"name":"Brinjal","name_ml":"വഴുതന","price":45,"image": baseURL + "brinjal-256.png","unit":"1 kg"},
        {"id":13,"name":"Brinjal Big","name_ml":"വലിയ വഴുതന","price":50,"image": baseURL + "brinjalbig-256.png","unit":"1 kg"},
        {"id":14,"name":"Cabbage","name_ml":"കാബേജ്","price":25,"image": baseURL + "cabbage-256.png","unit":"1 pc"},
        {"id":15,"name":"Capsicum","name_ml":"കാപ്സിക്കം","price":80,"image": baseURL + "capsicum-256.png","unit":"1 kg"},
        {"id":16,"name":"Cluster Beans","name_ml":"കൊത്തമര","price":55,"image": baseURL + "clusterbeans-256.png","unit":"1 kg"},
        {"id":17,"name":"Coconut","name_ml":"തേങ്ങ","price":35,"image": baseURL + "coconut-256.png","unit":"1 pc"},
        {"id":18,"name":"Colocasia","name_ml":"ചേമ്പ്","price":60,"image": baseURL + "colocasia-256.png","unit":"1 kg"},
        {"id":19,"name":"Coriander Leaves","name_ml":"മല്ലിയില","price":15,"image": baseURL + "corianderleaves-256.png","unit":"1 bunch"},
        {"id":20,"name":"Cucumber","name_ml":"വെള്ളരിക്ക","price":35,"image": baseURL + "cucumber-256.png","unit":"1 kg"},
        {"id":21,"name":"Curry Leaves","name_ml":"കറിവേപ്പില","price":10,"image": baseURL + "curryleaves-256.png","unit":"1 bunch"},
        {"id":22,"name":"Drumsticks","name_ml":"മുരിങ്ങക്കായ","price":70,"image": baseURL + "drumsticks-256.png","unit":"250 gm"},
        {"id":23,"name":"Elephant Yam","name_ml":"ചേന","price":70,"image": baseURL + "elephantyam-256.png","unit":"1 kg"},
        {"id":24,"name":"French Beans","name_ml":"ബീൻസ്","price":60,"image": baseURL + "frenchbeans-256.png","unit":"1 kg"},
        {"id":25,"name":"Garlic","name_ml":"വെളുത്തുള്ളി","price":120,"image": baseURL + "garlic-256.png","unit":"250 gm"},
        {"id":26,"name":"Ginger","name_ml":"ഇഞ്ചി","price":100,"image": baseURL + "ginger-256.png","unit":"100 gm"},
        {"id":27,"name":"Green Chili","name_ml":"പച്ചമുളക്","price":80,"image": baseURL + "greenchill-256.png","unit":"250 gm"},
        {"id":28,"name":"Ivy Gourd","name_ml":"കോവയ്ക്ക","price":45,"image": baseURL + "ivygourd-256.png","unit":"1 kg"},
        {"id":29,"name":"Lemon","name_ml":"നാരങ്ങ","price":60,"image": baseURL + "lemon-256.png","unit":"1 pc"},
        {"id":30,"name":"Plantain","name_ml":"ഏത്തക്കായ","price":50,"image": baseURL + "plantain-256.png","unit":"1 kg"},
        {"id":31,"name":"Pumpkin","name_ml":"മത്തങ്ങ","price":40,"image": baseURL + "pumpkin-256.png","unit":"1 kg"},
        {"id":32,"name":"Snake Gourd","name_ml":"പടവലങ്ങ","price":50,"image": baseURL + "snakegourd-256.png","unit":"1 kg"},
        {"id":33,"name":"Sweet Potato","name_ml":"മധുരക്കിഴങ്ങ്","price":40,"image": baseURL + "sweetpotato-256.png","unit":"1 kg"}
    ]
    
    for i in items: i['updated_at'] = get_now()
    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(items))
    return "New List Ready!"
