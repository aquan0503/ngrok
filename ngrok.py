from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Xin chào! Tôi là Trần Anh Quân - 2212815."

if __name__ == '__main__':
    app.run(port=5000, debug=True)
