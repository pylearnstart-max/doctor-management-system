
from flask import Flask, request, jsonify
from service import DoctorService

app = Flask(__name__)

doctor_service = DoctorService()


# 1. GET ALL DOCTORS
@app.route("/doctors", methods=["GET"])
def get_all_doctors():

    doctors = doctor_service.get_all_doctors()

    result = []

    for doctor in doctors:
        result.append({
            "id": doctor[0],
            "name": doctor[1],
            "disease": doctor[2]
        })

    return jsonify(result), 200


# 2. GET DOCTOR BY ID
@app.route("/doctors/<int:doctor_id>", methods=["GET"])
def get_doctor_by_id(doctor_id):

    doctor = doctor_service.get_doctor_by_id(doctor_id)

    if doctor is None:
        return jsonify({
            "status": "error",
            "message": "Doctor Not Found"
        }), 404

    return jsonify({
        "id": doctor[0],
        "name": doctor[1],
        "disease": doctor[2]
    }), 200


# 3. ADD DOCTOR
@app.route("/doctors", methods=["POST"])
def add_doctor():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON"
        }), 400

    name = data.get("name")
    disease = data.get("disease")

    if not name or not disease:
        return jsonify({
            "status": "error",
            "message": "Name and Disease are required"
        }), 400

    result = doctor_service.add_doctor(name, disease)

    if result:
        return jsonify({
            "status": "success",
            "message": "Doctor Added Successfully"
        }), 201

    return jsonify({
        "status": "error",
        "message": "Doctor Insert Failed"
    }), 400


# 4. UPDATE DOCTOR
@app.route("/doctors/<int:doctor_id>", methods=["PUT"])
def update_doctor(doctor_id):

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON"
        }), 400

    name = data.get("name")
    disease = data.get("disease")

    if not name or not disease:
        return jsonify({
            "status": "error",
            "message": "Name and Disease are required"
        }), 400

    result = doctor_service.update_doctor(
        doctor_id, name, disease
    )

    if result:
        return jsonify({
            "status": "success",
            "message": "Doctor Updated Successfully"
        }), 200

    return jsonify({
        "status": "error",
        "message": "Doctor Not Found"
    }), 404


# 5. DELETE DOCTOR
@app.route("/doctors/<int:doctor_id>", methods=["DELETE"])
def delete_doctor(doctor_id):

    result = doctor_service.delete_doctor(doctor_id)

    if result:
        return jsonify({
            "status": "success",
            "message": "Doctor Deleted Successfully"
        }), 200

    return jsonify({
        "status": "error",
        "message": "Doctor Not Found"
    }), 404


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)
