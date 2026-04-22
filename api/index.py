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
    resp = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
    data = resp.json().get("result")
    return jsonify(json.loads(data) if data else [])

@app.route('/api/update', methods=['POST'])
def update_price():
    update_info = request.json
    item_id = int(update_info.get('id'))
    new_price = update_info.get('price')

    resp = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
    all_items = json.loads(resp.json().get("result") or "[]")
    
    updated = False
    for item in all_items:
        if item['id'] == item_id:
            item['price'] = str(new_price)
            item['updated_at'] = get_ist_time()
            updated = True
            break

    if updated:
        requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(all_items))
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 404

@app.route('/api/setup')
def setup():
    # 100+ Items Database
    initial_data = [
        {"id": 1, "title": "Tomato", "name_ml": "തക്കാളി", "name_en": "Tomato", "name_manglish": "Thakkali", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🍅"},
        {"id": 2, "title": "Onion", "name_ml": "സവാള", "name_en": "Onion", "name_manglish": "Savala", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🧅"},
        {"id": 3, "title": "Small Onion", "name_ml": "ചെറിയ ഉള്ളി", "name_en": "Shallots", "name_manglish": "Cheriya Ulli", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🧅"},
        {"id": 4, "title": "Potato", "name_ml": "ഉരുളക്കിഴങ്ങ്", "name_en": "Potato", "name_manglish": "Urulakkizhangu", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥔"},
        {"id": 5, "title": "Green Chilli", "name_ml": "പച്ചമുളക്", "name_en": "Green Chilli", "name_manglish": "Pachamulaku", "price": "0", "unit": "250 gm", "updated_at": "N/A", "emoji": "🌶️"},
        {"id": 6, "title": "Carrot", "name_ml": "കാരറ്റ്", "name_en": "Carrot", "name_manglish": "Carrot", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥕"},
        {"id": 7, "title": "Ginger", "name_ml": "ഇഞ്ചി", "name_en": "Ginger", "name_manglish": "Inchi", "price": "0", "unit": "100 gm", "updated_at": "N/A", "emoji": "🫚"},
        {"id": 8, "title": "Garlic", "name_ml": "വെളുത്തുള്ളി", "name_en": "Garlic", "name_manglish": "Veluthulli", "price": "0", "unit": "250 gm", "updated_at": "N/A", "emoji": "🧄"},
        {"id": 9, "title": "Cabbage", "name_ml": "കാബേജ്", "name_en": "Cabbage", "name_manglish": "Cabbage", "price": "0", "unit": "1 pc", "updated_at": "N/A", "emoji": "🥬"},
        {"id": 10, "title": "Cauliflower", "name_ml": "കോളിഫ്ലവർ", "name_en": "Cauliflower", "name_manglish": "Cauliflower", "price": "0", "unit": "1 pc", "updated_at": "N/A", "emoji": "🥦"},
        {"id": 11, "title": "Ladies Finger", "name_ml": "വെണ്ടയ്ക്ക", "name_en": "Ladies Finger", "name_manglish": "Vendakka", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥦"},
        {"id": 12, "title": "Brinjal", "name_ml": "വഴുതനങ്ങ", "name_en": "Brinjal", "name_manglish": "Vazhuthananga", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🍆"},
        {"id": 13, "title": "Beetroot", "name_ml": "ബീറ്റ്‌റൂട്ട്", "name_en": "Beetroot", "name_manglish": "Beetroot", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🍠"},
        {"id": 14, "title": "Cucumber", "name_ml": "വെള്ളരിക്ക", "name_en": "Cucumber", "name_manglish": "Vellarikka", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥒"},
        {"id": 15, "title": "Snake Gourd", "name_ml": "പടവലങ്ങ", "name_en": "Snake Gourd", "name_manglish": "Padavalanga", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🐍"},
        {"id": 16, "title": "Bitter Gourd", "name_ml": "കൈപ്പയ്ക്ക", "name_en": "Bitter Gourd", "name_manglish": "Kaippakka", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥒"},
        {"id": 17, "title": "Bottle Gourd", "name_ml": "ചുരയ്ക്ക", "name_en": "Bottle Gourd", "name_manglish": "Churakka", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🧴"},
        {"id": 18, "title": "Ash Gourd", "name_ml": "കുമ്പളങ്ങ", "name_en": "Ash Gourd", "name_manglish": "Kumbalanga", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🎃"},
        {"id": 19, "title": "Pumpkin", "name_ml": "മത്തങ്ങ", "name_en": "Pumpkin", "name_manglish": "Mathanga", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🎃"},
        {"id": 20, "title": "Beans", "name_ml": "ബീൻസ്", "name_en": "Beans", "name_manglish": "Beans", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🎋"},
        {"id": 21, "title": "Long Beans", "name_ml": "പയർ", "name_en": "Long Beans", "name_manglish": "Payar", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🎋"},
        {"id": 22, "title": "Drumstick", "name_ml": "മുരിങ്ങക്ക", "name_en": "Drumstick", "name_manglish": "Muringakka", "price": "0", "unit": "250 gm", "updated_at": "N/A", "emoji": "🎋"},
        {"id": 23, "title": "Curry Leaves", "name_ml": "കറിവേപ്പില", "name_en": "Curry Leaves", "name_manglish": "Kariveppila", "price": "0", "unit": "1 bunch", "updated_at": "N/A", "emoji": "🌿"},
        {"id": 24, "title": "Coriander", "name_ml": "മല്ലിയില", "name_en": "Coriander", "name_manglish": "Malliyila", "price": "0", "unit": "1 bunch", "updated_at": "N/A", "emoji": "🌿"},
        {"id": 25, "title": "Mint Leaves", "name_ml": "പുതിനയില", "name_en": "Mint Leaves", "name_manglish": "Puthinayila", "price": "0", "unit": "1 bunch", "updated_at": "N/A", "emoji": "🍃"},
        {"id": 26, "title": "Lemon", "name_ml": "നാരങ്ങ", "name_en": "Lemon", "name_manglish": "Narangga", "price": "0", "unit": "1 pc", "updated_at": "N/A", "emoji": "🍋"},
        {"id": 27, "title": "Green Papaya", "name_ml": "പച്ചപ്പപ്പായ", "name_en": "Raw Papaya", "name_manglish": "Pacha Pappaya", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🍈"},
        {"id": 28, "title": "Yam", "name_ml": "ചേന", "name_en": "Yam", "name_manglish": "Chena", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🍠"},
        {"id": 29, "title": "Colocasia", "name_ml": "ചേമ്പ്", "name_en": "Colocasia", "name_manglish": "Chembu", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🍠"},
        {"id": 30, "title": "Sweet Potato", "name_ml": "മധുരക്കിഴങ്ങ്", "name_en": "Sweet Potato", "name_manglish": "Madhurakkizhangu", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🍠"},
        {"id": 31, "title": "Raw Banana", "name_ml": "പച്ചക്കായ", "name_en": "Raw Banana", "name_manglish": "Pachakkaya", "price": "0", "unit": "1 pc", "updated_at": "N/A", "emoji": "🍌"},
        {"id": 32, "title": "Banana Flower", "name_ml": "വാഴപ്പൂവ്", "name_en": "Banana Flower", "name_manglish": "Vazhappoovu", "price": "0", "unit": "1 pc", "updated_at": "N/A", "emoji": "🌺"},
        {"id": 33, "title": "Banana Stem", "name_ml": "വാഴപ്പിണ്ടി", "name_en": "Banana Stem", "name_manglish": "Vazhappindi", "price": "0", "unit": "1 pc", "updated_at": "N/A", "emoji": "🪵"},
        {"id": 34, "title": "Ivy Gourd", "name_ml": "കോവയ്ക്ക", "name_en": "Ivy Gourd", "name_manglish": "Kovakka", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥒"},
        {"id": 35, "title": "Radish", "name_ml": "മുള്ളങ്കി", "name_en": "Radish", "name_manglish": "Mullangi", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥕"},
        {"id": 36, "title": "Mushroom", "name_ml": "കൂൺ", "name_en": "Mushroom", "name_manglish": "Koon", "price": "0", "unit": "1 pkt", "updated_at": "N/A", "emoji": "🍄"},
        {"id": 37, "title": "Capsicum", "name_ml": "ക്യാപ്സിക്കം", "name_en": "Capsicum", "name_manglish": "Capsicum", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🫑"},
        {"id": 38, "title": "Green Peas", "name_ml": "പച്ചപ്പയർ", "name_en": "Green Peas", "name_manglish": "Pacha Payar", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🫛"},
        {"id": 39, "title": "Spinach", "name_ml": "ചീര", "name_en": "Spinach", "name_manglish": "Cheera", "price": "0", "unit": "1 bunch", "updated_at": "N/A", "emoji": "🥬"},
        {"id": 40, "title": "Broccoli", "name_ml": "ബ്രോക്കോളി", "name_en": "Broccoli", "name_manglish": "Broccoli", "price": "0", "unit": "1 pc", "updated_at": "N/A", "emoji": "🥦"}
        # Note: You can keep adding more here to reach 100...
    ]
    
    # Adding extra items to reach a higher count for sample
    for i in range(41, 101):
        initial_data.append({"id": i, "title": f"Veg Item {i}", "name_ml": f"പച്ചക്കറി {i}", "name_en": f"Vegetable {i}", "name_manglish": f"Veg {i}", "price": "0", "unit": "1 kg", "updated_at": "N/A", "emoji": "🥗"})

    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(initial_data))
    return "100 Items Setup Complete!"

def handler(event, context):
    return app(event, context)
