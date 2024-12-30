from flask import Flask
from rotas import clima
app = Flask(__name__)

app.register_blueprint(clima)

app.run(debug=True)