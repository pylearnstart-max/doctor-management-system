
from flask import Blueprint, request, jsonify
from patient_service import PatientService
import traceback

patient_bp = Blueprint("patient", __name__)

service = PatientService()


# 1. ADD PATIENT
@patient_bp.route("/patients", methods=["POST"])
def add_patient():

    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "status": "error",
                "message": "Please provide valid JSON data"
            }), 400

        patient_id = service.add_patient(data)

        return jsonify({
            "status": "success",
            "message": "Patient added successfully",
            "patient_id": patient_id
        }), 201

    except ValueError as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:
        print("ADD PATIENT ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500


# 2. GET ALL PATIENTS
@patient_bp.route("/patients", methods=["GET"])
def get_all_patients():

    try:
        patients = service.get_all_patients()

        return jsonify({
            "status": "success",
            "count": len(patients),
            "data": patients
        }), 200

    except Exception as e:
        print("GET ALL PATIENTS ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500


# 3. GET PATIENT BY ID
@patient_bp.route("/patients/<int:patient_id>", methods=["GET"])
def get_patient_by_id(patient_id):

    try:
        patient = service.get_patient_by_id(patient_id)

        return jsonify({
            "status": "success",
            "data": patient
        }), 200

    except ValueError as e:
        status_code = 404 if str(e) == "Patient not found" else 400

        return jsonify({
            "status": "error",
            "message": str(e)
        }), status_code

    except Exception as e:
        print("GET PATIENT BY ID ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500


# 4. UPDATE PATIENT
@patient_bp.route("/patients/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):

    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "status": "error",
                "message": "Please provide valid JSON data"
            }), 400

        service.update_patient(patient_id, data)

        return jsonify({
            "status": "success",
            "message": "Patient updated successfully"
        }), 200

    except ValueError as e:
        status_code = 404 if str(e) == "Patient not found" else 400

        return jsonify({
            "status": "error",
            "message": str(e)
        }), status_code

    except Exception as e:
        print("UPDATE PATIENT ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500


# 5. DELETE PATIENT
@patient_bp.route("/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):

    try:
        service.delete_patient(patient_id)

        return jsonify({
            "status": "success",
            "message": "Patient deleted successfully"
        }), 200

    except ValueError as e:
        status_code = 404 if str(e) == "Patient not found" else 400

        return jsonify({
            "status": "error",
            "message": str(e)
        }), status_code

    except Exception as e:
        print("DELETE PATIENT ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500
