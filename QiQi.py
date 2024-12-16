from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    seatalk_challenge = data.get('seatalk_challenge')
    if seatalk_challenge:
        return seatalk_challenge, 200
    return "Invalid request", 400

if __name__ == '__main__':
    app.run()
