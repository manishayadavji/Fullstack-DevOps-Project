from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/status')
def status():
    return jsonify({"message": "Backend is Running on Port 5000", "db_status": "Connected"})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
