from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   url_for)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
cors = CORS(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):  # constructor
        self.name = name
        self.email = email
        self.phone = phone


@app.route("/", methods=['GET'])
def Index():
    all_data = Data.query.all()
    return render_template("index.html", data=all_data)


# insert data to database
@app.route("/insert", methods=['POST'])
def insert():
    if(request.method == 'POST'):
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash('Record inserted successfully')

        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)  # debug=True
