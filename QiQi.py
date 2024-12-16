from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    data = request.get_json()
    print("Received data:", data)  # In dữ liệu nhận được ra console để debug

    if not data:
        return "No JSON data received", 400

    seatalk_challenge = data.get('seatalk_challenge')
    if seatalk_challenge:
        return seatalk_challenge, 200

    return "seatalk_challenge not found in request", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
