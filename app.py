from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 'sqlite:///C:\\Users\\me\\PycharmProjects\\thisproject\\database.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
drone_medication = db.Table('drone-medication',
                            db.Column('drone_id', db.Integer, db.ForeignKey('drone.id')),
                            db.Column('medication_id', db.Integer, db.ForeignKey('medication.id'))
                            )


class Drone(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String(100))
    model = db.Column(db.String)
    weight_limit = db.Column(db.String)
    battery_capacity = db.Column(db.String)
    state = db.Column(db.String)
    following = db.relationship('Medication', secondary=drone_medication, backref='followers')


class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    weight = db.Column(db.Integer)
    code = db.Column(db.String)
    image = db.Column(db.String)


app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_message_from_drone():
    return jsonify({"message": "hellow"})


if __name__ == "__main__":
    app.run(debug=True)
