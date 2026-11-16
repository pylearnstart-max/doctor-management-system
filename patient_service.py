
from patient_repository import PatientRepository
from patient_model import Patient


class PatientService:

    def __init__(self):

        self.repo = PatientRepository()

    # 1. ADD PATIENT
    def add_patient(self, data):

        if not isinstance(data, dict):
            raise ValueError("Invalid patient data")

        patient_name = data.get("patient_name")

        if not isinstance(patient_name, str) or not patient_name.strip():
            raise ValueError("Patient name is required")

        age = data.get("age")

        if age is not None:
            if type(age) != int or age < 0 or age > 130:
                raise ValueError("Enter a valid patient age")

        phone = data.get("phone")

        if not isinstance(phone, str) or not phone.isdigit() or len(phone) != 10:
            raise ValueError("Enter a valid 10-digit phone number")

        patient = Patient(
            patient_name=patient_name.strip(),
            age=age,
            gender=data.get("gender"),
            phone=phone,
            email=data.get("email"),
            address=data.get("address"),
            disease=data.get("disease")
        )

        return self.repo.add_patient(patient)

    # 2. GET ALL PATIENTS
    def get_all_patients(self):

        return self.repo.get_all_patients()

    # 3. GET PATIENT BY ID
    def get_patient_by_id(self, patient_id):

        if type(patient_id) != int or patient_id <= 0:
            raise ValueError("Invalid patient ID")

        patient = self.repo.get_patient_by_id(patient_id)

        if patient is None:
            raise ValueError("Patient not found")

        return patient

    # 4. UPDATE PATIENT
    def update_patient(self, patient_id, data):

        if type(patient_id) != int or patient_id <= 0:
            raise ValueError("Invalid patient ID")

        if not isinstance(data, dict):
            raise ValueError("Invalid patient data")

        patient_name = data.get("patient_name")

        if not isinstance(patient_name, str) or not patient_name.strip():
            raise ValueError("Patient name is required")

        age = data.get("age")

        if age is not None:
            if type(age) != int or age < 0 or age > 130:
                raise ValueError("Enter a valid patient age")

        phone = data.get("phone")

        if not isinstance(phone, str) or not phone.isdigit() or len(phone) != 10:
            raise ValueError("Enter a valid 10-digit phone number")

        existing_patient = self.repo.get_patient_by_id(patient_id)

        if existing_patient is None:
            raise ValueError("Patient not found")

        patient = Patient(
            patient_name=patient_name.strip(),
            age=age,
            gender=data.get("gender"),
            phone=phone,
            email=data.get("email"),
            address=data.get("address"),
            disease=data.get("disease")
        )

        return self.repo.update_patient(patient_id, patient)

    # 5. DELETE PATIENT
    def delete_patient(self, patient_id):

        if type(patient_id) != int or patient_id <= 0:
            raise ValueError("Invalid patient ID")

        existing_patient = self.repo.get_patient_by_id(patient_id)

        if existing_patient is None:
            raise ValueError("Patient not found")

        return self.repo.delete_patient(patient_id)
