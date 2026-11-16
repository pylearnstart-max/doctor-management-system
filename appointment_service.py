
from appointment_repository import AppointmentRepository
from appointment_model import Appointment
from datetime import datetime


class AppointmentService:

    def __init__(self):
        self.repo = AppointmentRepository()

    # 1. ADD APPOINTMENT
    def add_appointment(self, data):

        if not isinstance(data, dict):
            raise ValueError("Invalid appointment data")

        patient_id = data.get("patient_id")
        doctor_id = data.get("DoctorID")

        if type(patient_id) != int or patient_id <= 0:
            raise ValueError("Valid patient ID is required")

        if type(doctor_id) != int or doctor_id <= 0:
            raise ValueError("Valid doctor ID is required")

        appointment_date = data.get("appointment_date")
        appointment_time = data.get("appointment_time")

        try:
            appointment_date = datetime.strptime(
                appointment_date, "%Y-%m-%d"
            ).date()

            appointment_time = datetime.strptime(
                appointment_time, "%H:%M"
            ).time()

        except (ValueError, TypeError):
            raise ValueError(
                "Date format must be YYYY-MM-DD and time format HH:MM"
            )

        reason = data.get("reason")
        status = data.get("status", "Scheduled")

        if status not in ["Scheduled", "Completed", "Cancelled"]:
            raise ValueError("Invalid appointment status")

        appointment = Appointment(
            patient_id=patient_id,
            DoctorID=doctor_id,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason,
            status=status
        )

        return self.repo.add_appointment(appointment)

    # 2. GET ALL APPOINTMENTS
    def get_all_appointments(self):

        return self.repo.get_all_appointments()

    # 3. GET APPOINTMENT BY ID
    def get_appointment_by_id(self, appointment_id):

        if type(appointment_id) != int or appointment_id <= 0:
            raise ValueError("Invalid appointment ID")

        appointment = self.repo.get_appointment_by_id(
            appointment_id
        )

        if appointment is None:
            raise ValueError("Appointment not found")

        return appointment

    # 4. UPDATE APPOINTMENT
    def update_appointment(self, appointment_id, data):

        if type(appointment_id) != int or appointment_id <= 0:
            raise ValueError("Invalid appointment ID")

        if not isinstance(data, dict):
            raise ValueError("Invalid appointment data")

        existing = self.repo.get_appointment_by_id(appointment_id)

        if existing is None:
            raise ValueError("Appointment not found")

        patient_id = data.get("patient_id")
        doctor_id = data.get("DoctorID")

        if type(patient_id) != int or patient_id <= 0:
            raise ValueError("Valid patient ID is required")

        if type(doctor_id) != int or doctor_id <= 0:
            raise ValueError("Valid doctor ID is required")

        try:
            appointment_date = datetime.strptime(
                data.get("appointment_date"), "%Y-%m-%d"
            ).date()

            appointment_time = datetime.strptime(
                data.get("appointment_time"), "%H:%M"
            ).time()

        except (ValueError, TypeError):
            raise ValueError(
                "Date format must be YYYY-MM-DD and time format HH:MM"
            )

        reason = data.get("reason")
        status = data.get("status")

        if status not in ["Scheduled", "Completed", "Cancelled"]:
            raise ValueError("Invalid appointment status")

        appointment = Appointment(
            patient_id=patient_id,
            DoctorID=doctor_id,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason,
            status=status
        )

        updated = self.repo.update_appointment(
            appointment_id, appointment
        )

        if not updated:
            raise ValueError("Appointment not found")

        return True

    # 5. DELETE APPOINTMENT
    def delete_appointment(self, appointment_id):

        if type(appointment_id) != int or appointment_id <= 0:
            raise ValueError("Invalid appointment ID")

        existing = self.repo.get_appointment_by_id(appointment_id)

        if existing is None:
            raise ValueError("Appointment not found")

        return self.repo.delete_appointment(appointment_id)
