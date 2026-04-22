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
    # IST സമയം സെറ്റ് ചെയ്യുന്നു
    return datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d %b, %I:%M %p")

@app.route('/api/veg', methods=['GET'])
def fetch_all():
    try:
        r = requests.get(f"{UPSTASH_URL}/get/vegetables", headers=headers)
        res_data = r.json().get("result")
        return jsonify(json.loads(res_data) if res_data else [])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/save-all', methods=['POST'])
def save_all():
    try:
        items = request.json
        last_sync = get_now()
        
        # ഓരോ ഐറ്റത്തിനും ലാസ്റ്റ് അപ്‌ഡേറ്റ് സമയം നൽകുന്നു
        for i in items:
            i['last_updated'] = last_sync
            
        # Upstash-ലേക്ക് സേവ് ചെയ്യുന്നു
        requests.post(f"{UPSTASH_URL}/set/vegetables", 
                      headers=headers, 
                      data=json.dumps(items))
        
        return jsonify({"status": "success", "time": last_sync})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # പ്രൊഡക്ഷനിൽ പോകുമ്പോൾ debug=False ആക്കുക
    app.run(host='0.0.0.0', port=5000, debug=True)
