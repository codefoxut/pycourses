import pandas
import geopy
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/success', methods=["POST"])
def success():
    global file1
    message = "Please choose right method to call success."
    if request.method == "POST":
        file1 = request.files["file"]
        print(type(file1))
        if file1.mimetype == 'text/csv':
            df = pandas.read_csv(file1)
            if "address" in df.columns:
                df["Address"] = df["address"]
                address = True
            elif "Address" in df.columns:
                address = True
            else:
                address = False
                message = "Please include address in your csv."
            if address:
                from geopy.geocoders import ArcGIS
                nom = ArcGIS()
                coordinates = df["Address"].apply(nom.geocode)
                df["Latitude"] = coordinates.apply(lambda x: x.latitude if x is not None else None)
                df["Longitude"] = coordinates.apply(lambda x: x.longitude if x is not None else None)

                fname = "uploaded/" + secure_filename(f"uploaded_{file1.filename}")
                df.to_csv(fname, index=None)
                return render_template("index.html", data=df.to_html(), btn="download.html")
        else:
            message = "Please upload correct csv file."
    return render_template("index.html", text=message)


@app.route("/download")
def download():
    fname = "uploaded/" + secure_filename(f"uploaded_{file1.filename}")
    return send_file(fname, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
