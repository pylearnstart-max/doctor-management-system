
from flask import Flask

# Import existing Doctor Flask application
from api import app as doctor_app

# Import Patient Blueprint
from patient_api import patient_bp

# Import Appointment Blueprint
from appointment_api import appointment_bp


app = Flask(__name__)


# Register existing Doctor API routes
for rule in doctor_app.url_map.iter_rules():

    if rule.endpoint == "static":
        continue

    view_function = doctor_app.view_functions[rule.endpoint]

    app.add_url_rule(
        rule.rule,
        endpoint=f"doctor_{rule.endpoint}",
        view_func=view_function,
        methods=[
            method
            for method in rule.methods
            if method not in ("HEAD", "OPTIONS")
        ]
    )


# Register Patient APIs
app.register_blueprint(patient_bp)


# Register Appointment APIs
app.register_blueprint(appointment_bp)


# Home API
@app.route("/", methods=["GET"])
def home():

    return {
        "status": "success",
        "message": "Clinic Management System API is running",
        "modules": [
            "Doctor Management",
            "Patient Management",
            "Appointment Management"
        ]
    }


if __name__ == "__main__":

    print(app.url_map)

    app.run(debug=True)
