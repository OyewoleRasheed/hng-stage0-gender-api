from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timezone
import requests
import os

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

GENDERIZE_API_URL = "https://api.genderize.io"


def get_gender(name):
    response = requests.get(f"{GENDERIZE_API_URL}?name={name}")
    return response.json()


@app.route('/api/classify', methods=['GET'])
def classify():
    name = request.args.get('name')

    if not name:
        return jsonify({"status": "error", "message": "<400 Bad Request>"}), 400

    if type(name) != str:
        return jsonify({"status": "error", "message": "<422 Unprocessable Entity>"}), 422

    gender_data = get_gender(name)
    if gender_data is None:
        return jsonify({"status": "error", "message": "<Failed to reach classification service>"}), 502

    probability = gender_data['probability']
    count = gender_data['count']
    gender = gender_data['gender']

    if gender is None or count == 0:
        return jsonify({"status": "error", "message": "<No prediction available for the provided name>"}), 404

    if probability >= 0.7 and count >= 100:
        is_confident = True
    else:
        is_confident = False

    processed_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    return jsonify({
        "status": "success",
        "data": {
            "name": f"<{name}>",
            "gender": gender,
            "probability": probability,
            "sample_size": count,
            "is_confident": is_confident,
            "processed_at": processed_at
        }
    }), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)