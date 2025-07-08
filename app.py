import os
from flask import Flask
from controllers import controllers

app = Flask(__name__)
app.register_blueprint(controllers)

@app.route("/")
def home():
    return "Hola desde Railway!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
