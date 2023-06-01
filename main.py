from flask import Flask, render_template, send_from_directory;
import json
from datetime import datetime

app = Flask(__name__)

@app.get("/")
def index():
    manifest = json.load(open("./statics/dist/manifest.json", "rb"))
    kwargs = {"main": manifest["js/main.js"]["file"], "style": manifest["js/main.css"]["file"]}
    return render_template("index.html", **kwargs)
    
@app.get("/get-server-time")
def cool():
    return {"status": "success", "time": datetime.utcnow()}

@app.get("/assets/<path:path>")
def statics(path):
    return send_from_directory('statics/dist/assets', path)
    
if __name__ == "__main__":
    app.run(debug=True, port=5555)