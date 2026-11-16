
class Patient:

    def __init__(
        self,
        patient_id=None,
        patient_name=None,
        age=None,
        gender=None,
        phone=None,
        email=None,
        address=None,
        disease=None
    ):

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
        self.disease = disease

    def to_dict(self):

        return {
            "patient_id": self.patient_id,
            "patient_name": self.patient_name,
            "age": self.age,
            "gender": self.gender,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "disease": self.disease
        }
