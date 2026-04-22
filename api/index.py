from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import requests
import pytz

app = Flask(__name__)
# എല്ലാ ഒറിജിനലുകളെയും (Any Port/Any IP) അനുവദിക്കാൻ ഈ സെറ്റിംഗ്സ് സഹായിക്കും
CORS(app, resources={r"/api/*": {"origins": "*"}})

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
    except Exception as e:
        print(f"Error fetching: {e}")
        return jsonify([])

@app.route('/api/save-all', methods=['POST'])
def save_all():
    try:
        items = request.json
        last_sync = get_now()
        for i in items:
            # പുതിയ അപ്‌ഡേറ്റ് ടൈം ഓരോ ഐറ്റത്തിലും ചേർക്കുന്നു
            i['last_updated'] = last_sync
            
        requests.post(f"{UPSTASH_URL}/set/vegetables", headers=headers, data=json.dumps(items))
        return jsonify({"status": "success", "time": last_sync})
    except Exception as e:
        print(f"Error saving: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Flask 5000 പോർട്ടിൽ റൺ ആകുന്നു
    app.run(host='0.0.0.0', port=5000, debug=True)
