from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "hello world"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
