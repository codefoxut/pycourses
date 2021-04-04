
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/plot/')
def plot():
    from .plot_sensex_data import plot_data
    script1, div1, cdn_js = plot_data()
    return render_template("plot.html", script1=script1, div1=div1, cdn_js=cdn_js[0])


if __name__ == "__main__":
    app.run(debug=True)
