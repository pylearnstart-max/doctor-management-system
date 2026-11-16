
from flask import Blueprint, request, jsonify
from appointment_service import AppointmentService
import traceback

appointment_bp = Blueprint("appointment", __name__)

service = AppointmentService()


# 1. ADD APPOINTMENT - POST
@appointment_bp.route("/appointments", methods=["POST"])
def add_appointment():

    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "status": "error",
                "message": "Please provide valid JSON"
            }), 400

        appointment_id = service.add_appointment(data)

        return jsonify({
            "status": "success",
            "message": "Appointment booked successfully",
            "appointment_id": appointment_id
        }), 201

    except ValueError as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

    except Exception as e:
        print("ADD APPOINTMENT ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500


# 2. GET ALL APPOINTMENTS
@appointment_bp.route("/appointments", methods=["GET"])
def get_all_appointments():

    try:
        appointments = service.get_all_appointments()

        return jsonify({
            "status": "success",
            "count": len(appointments),
            "data": appointments
        }), 200

    except Exception as e:
        print("GET APPOINTMENTS ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500


# 3. GET APPOINTMENT BY ID
@appointment_bp.route(
    "/appointments/<int:appointment_id>",
    methods=["GET"]
)
def get_appointment_by_id(appointment_id):

    try:
        appointment = service.get_appointment_by_id(
            appointment_id
        )

        return jsonify({
            "status": "success",
            "data": appointment
        }), 200

    except ValueError as e:
        status_code = (
            404 if str(e) == "Appointment not found" else 400
        )

        return jsonify({
            "status": "error",
            "message": str(e)
        }), status_code

    except Exception as e:
        print("GET APPOINTMENT ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500


# 4. UPDATE APPOINTMENT - PUT
@appointment_bp.route(
    "/appointments/<int:appointment_id>",
    methods=["PUT"]
)
def update_appointment(appointment_id):

    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "status": "error",
                "message": "Please provide valid JSON"
            }), 400

        service.update_appointment(appointment_id, data)

        return jsonify({
            "status": "success",
            "message": "Appointment updated successfully"
        }), 200

    except ValueError as e:
        status_code = (
            404 if str(e) == "Appointment not found" else 400
        )

        return jsonify({
            "status": "error",
            "message": str(e)
        }), status_code

    except Exception as e:
        print("UPDATE APPOINTMENT ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500


# 5. DELETE APPOINTMENT
@appointment_bp.route(
    "/appointments/<int:appointment_id>",
    methods=["DELETE"]
)
def delete_appointment(appointment_id):

    try:
        service.delete_appointment(appointment_id)

        return jsonify({
            "status": "success",
            "message": "Appointment deleted successfully"
        }), 200

    except ValueError as e:
        status_code = (
            404 if str(e) == "Appointment not found" else 400
        )

        return jsonify({
            "status": "error",
            "message": str(e)
        }), status_code

    except Exception as e:
        print("DELETE APPOINTMENT ERROR:", e)
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500
