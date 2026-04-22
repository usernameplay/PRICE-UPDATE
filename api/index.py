from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import requests
import pytz

app = Flask(__name__)
CORS(app)

# Upstash Database Config
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
    items = request.json
    last_sync = get_now()
    for i in items:
        # Update timestamp for changed items (simple logic)
        i['updated_at'] = last_sync
            
    requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(items))
    return jsonify({"status": "success", "time": last_sync})
