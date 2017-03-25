import os, ocr
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/welcome')
def welcome():
    return app.send_static_file('index.html')

@app.route('/ocr', methods=['GET', 'POST'])
def do_ocr():
    image = 'static/images/bet2.jpg'
    ocr_obj = ocr.OCR(image)
    text = ocr_obj.ocr()
    data = {'time': '12:25', 'track': 'kempton', 'selection': 'Shergar', 'odds': '21/20'}
    return jsonify(ocr=data)

port = os.getenv('PORT', '8080')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))

