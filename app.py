from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)
drone_medication=db.Table('drone-medication',
                              db.Column('drone_id', db.Integer, db.ForeignKey('drone.id')),
                              db.Column('medication_id', db.Integer, db.ForeignKey('medication.id'))
)


class drone(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String(100))
    model = db.column(db.String)
    weight_limit = db.column(db.String)
    battery_capacity = db.column(db.String)
    state = db.column(db.String)
    following=db.relationship('medication',secondary=drone_medication, backref='followers')

   
class medication(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.column(db.text)
    weight = db.column(db.Integer)
    code = db.column(db.String)
    image = db.Column(db.String)

    

@app.route("/drone-service", methods = ["GET"])
def get_message_from_drone():
    return jsonify({"message": "hellow"})

if __name__ == "__main__":
    app.run(debug=True)
