from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/movimentar/<int:x>/<int:y>/<int:z>/', methods=["POST"])
def movimentar(x, y, z):
    return f'{x}, {y}, {z}!'

if __name__ == '__main__':
    app.run(debug=True)