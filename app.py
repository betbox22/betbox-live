from flask import Flask, jsonify, send_from_directory
from color_logic_live import sample_games
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/games')
def games():
    return jsonify(sample_games())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
