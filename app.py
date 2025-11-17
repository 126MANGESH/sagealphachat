from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Renders templates/index.html
    return render_template("index.html")

if __name__ == "__main__":
    # Use 0.0.0.0 and port 8000 for Azure
    app.run(host="0.0.0.0", port=8000)
