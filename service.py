
from repository import DoctorRepository


class DoctorService:

    def __init__(self):
        self.repo = DoctorRepository()

    # 1. ADD DOCTOR
    def add_doctor(self, name, disease):

        if not name or not disease:
            return False

        return self.repo.add_doctor(name, disease)

    # 2. GET ALL DOCTORS
    def get_all_doctors(self):

        return self.repo.get_all_doctors()

    # 3. GET DOCTOR BY ID
    def get_doctor_by_id(self, doctor_id):

        if doctor_id <= 0:
            return None

        return self.repo.get_doctor_by_id(doctor_id)

    # 4. UPDATE DOCTOR
    def update_doctor(self, doctor_id, name, disease):

        if doctor_id <= 0 or not name or not disease:
            return False

        return self.repo.update_doctor(
            doctor_id, name, disease
        )

    # 5. DELETE DOCTOR
    def delete_doctor(self, doctor_id):

        if doctor_id <= 0:
            return False

        return self.repo.delete_doctor(doctor_id)
