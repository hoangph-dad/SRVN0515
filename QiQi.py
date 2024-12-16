from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Railway!"

@app.route('/callback', methods=['POST'])
def callback():
    try:
        # Lấy dữ liệu JSON từ request
        data = request.get_json()
        print("Received data:", data)

        # Lấy seatalk_challenge từ nested JSON
        seatalk_challenge = data.get('event', {}).get('seatalk_challenge')

        # Kiểm tra nếu seatalk_challenge tồn tại và trả về đúng định dạng
        if seatalk_challenge:
            return jsonify({"seatalk_challenge": seatalk_challenge}), 200

        return "seatalk_challenge not found in request", 400

    except Exception as e:
        # Trả về lỗi chi tiết nếu có exception
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Railway sẽ cung cấp cổng qua biến môi trường PORT
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
