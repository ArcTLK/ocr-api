from flask import Flask, request, jsonify
from flask_cors import CORS
from ocr import getText
import uuid
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        filePath = './images/{}.png'.format(str(uuid.uuid4()))
        file.save(filePath)
        return jsonify(getText(filePath))
    return 'Hello World'
