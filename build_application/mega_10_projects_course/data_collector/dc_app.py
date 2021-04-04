
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/testdb'

db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Float)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload')
def file_upload():
    return render_template("file_upload.html")


@app.route('/file_success', methods=["POST"])
def file_success():
    if request.method == 'POST':
        file1 = request.files["file_name"]
        file1.save("uploaded_files/" + secure_filename("uploaded"+file1.filename))
        return render_template("success.html")


@app.route('/success', methods=["POST"])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        print(email, height)
        if not db.session.query(Data).filter(Data.email_ == email).count():
            d = Data(email, height)
            db.session.add(d)
            db.session.commit()
            return render_template("success.html")
        return render_template("index.html", text="We already have data for this email.")


if __name__ == "__main__":
    app.run(debug=True)
