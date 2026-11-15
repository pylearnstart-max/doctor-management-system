from repository import DoctorRepository


class DoctorService:

    def __init__(self):
        self.repo = DoctorRepository()

    # 1. ADD DOCTOR
    def add_doctor(self, name, disease):

        if not name or not disease:
            return False

        return self.repo.add_doctor(name.strip(), disease.strip())

    # 2. GET ALL DOCTORS
    def get_all_doctors(self):

        return self.repo.get_all_doctors()

    # 3. GET DOCTOR BY ID
    def get_doctor_by_id(self, doctor_id):

        if not isinstance(doctor_id, int) or doctor_id <= 0:
            return None

        return self.repo.get_doctor_by_id(doctor_id)

    # 4. UPDATE DOCTOR
    def update_doctor(self, doctor_id, name, disease):

        if not isinstance(doctor_id, int) or doctor_id <= 0:
            return False

        if not name or not disease:
            return False

        return self.repo.update_doctor(
            doctor_id, name.strip(), disease.strip()
        )

    # 5. DELETE DOCTOR
    def delete_doctor(self, doctor_id):

        if not isinstance(doctor_id, int) or doctor_id <= 0:
            return False

        return self.repo.delete_doctor(doctor_id)

    # 6. SEARCH BY NAME
    def search_doctor_by_name(self, name):

        if not isinstance(name, str) or not name.strip():
            return []

        return self.repo.search_doctor_by_name(name.strip())

    # 7. SEARCH BY DISEASE
    def search_doctor_by_disease(self, disease):

        if not isinstance(disease, str) or not disease.strip():
            return []

        return self.repo.search_doctor_by_disease(disease.strip())

    # 8. TOTAL DOCTOR COUNT
    def get_doctor_count(self):

        return self.repo.get_doctor_count()