from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/browse-items")
def browse():
    return render_template("browse-items.html")

@app.route("/report-items")
def report():
    return render_template("report-items.html")


if __name__ == "__main__":
    app.run(debug=True)