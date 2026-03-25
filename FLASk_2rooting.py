12. ROUTING DI FLASK

Routing adalah pengaturan alamat URL.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Halaman Home"

@app.route('/about')
def about():
    return "Halaman About"

if __name__ == '__main__':
    app.run(debug=True)
