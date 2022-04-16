from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/crud-flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):  # constructor
        self.name = name
        self.email = email
        self.phone = phone


@app.route("/")
def Index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)  # debug=True
