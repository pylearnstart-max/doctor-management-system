
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

    if not isinstance(data, dict):
        return jsonify({
            "status": "error",
            "message": "Invalid JSON"
        }), 400

    name = data.get("name")
    disease = data.get("disease")

    if (not isinstance(name, str) or not name.strip()
            or not isinstance(disease, str) or not disease.strip()):
        return jsonify({
            "status": "error",
            "message": "Name and Disease are required"
        }), 400

    result = doctor_service.add_doctor(
        name.strip(), disease.strip()
    )

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

    if not isinstance(data, dict):
        return jsonify({
            "status": "error",
            "message": "Invalid JSON"
        }), 400

    name = data.get("name")
    disease = data.get("disease")

    if (not isinstance(name, str) or not name.strip()
            or not isinstance(disease, str) or not disease.strip()):
        return jsonify({
            "status": "error",
            "message": "Name and Disease are required"
        }), 400

    result = doctor_service.update_doctor(
        doctor_id, name.strip(), disease.strip()
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


# 6. SEARCH DOCTOR BY NAME
@app.route("/doctors/search/name/<string:name>", methods=["GET"])
def search_doctor_by_name(name):

    if not name.strip():
        return jsonify({
            "status": "error",
            "message": "Name is required"
        }), 400

    doctors = doctor_service.search_doctor_by_name(name.strip())

    result = []

    for doctor in doctors:
        result.append({
            "id": doctor[0],
            "name": doctor[1],
            "disease": doctor[2]
        })

    return jsonify(result), 200


# 7. SEARCH DOCTOR BY DISEASE
@app.route("/doctors/search/disease/<string:disease>", methods=["GET"])
def search_doctor_by_disease(disease):

    if not disease.strip():
        return jsonify({
            "status": "error",
            "message": "Disease is required"
        }), 400

    doctors = doctor_service.search_doctor_by_disease(
        disease.strip()
    )

    result = []

    for doctor in doctors:
        result.append({
            "id": doctor[0],
            "name": doctor[1],
            "disease": doctor[2]
        })

    return jsonify(result), 200


# 8. GET TOTAL DOCTOR COUNT
@app.route("/doctors/count", methods=["GET"])
def get_doctor_count():

    count = doctor_service.get_doctor_count()

    return jsonify({
        "status": "success",
        "total_doctors": count
    }), 200


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)
