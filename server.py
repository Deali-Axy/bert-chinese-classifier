from flask import Flask, jsonify, request
from core.predictor import Predictor
from config import train_config

app = Flask(__name__)
predictor = Predictor(train_config)


@app.route('/', methods=['GET'])
def predict():
    text = request.form.get('text')
    response = {
        'result': predictor.predict(text)
    }

    return jsonify(response), 201


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
