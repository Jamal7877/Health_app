from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/healthcare_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ----------------------------
# Database Models
# ----------------------------
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dob = db.Column(db.String(20))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    doctor = db.Column(db.String(100))

# Initialize tables
with app.app_context():
    db.create_all()

# Sample users
users = {"admin": "password123", "doctor": "medic2024"}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            new_patient = Patient(
                name=request.form["name"],
                dob=request.form["dob"],
                address=request.form["address"],
                phone=request.form["phone"]
            )
            db.session.add(new_patient)
            db.session.commit()
            return redirect(url_for("dashboard"))
        except Exception as e:
            print("Error during registration:", e)
            return "Registration failed. Check your console."
    return render_template("register.html")

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        try:
            new_appointment = Appointment(
                patient_id=request.form["patient_id"],
                date=request.form["date"],
                time=request.form["time"],
                doctor=request.form["doctor"]
            )
            db.session.add(new_appointment)
            db.session.commit()
            return redirect(url_for("dashboard"))
        except Exception as e:
            print("Error during appointment creation:", e)
            return "Appointment creation failed. Check your console."
    return render_template("appointment.html")

if __name__ == "__main__":
    app.run(debug=True)
