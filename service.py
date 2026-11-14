


from repository import DoctorRepository


class DoctorService:

    def __init__(self):
        self.repo = DoctorRepository()


    # 1. INSERT DOCTOR
    def add_doctor(self, name, disease):

        if not name or not disease:
            print("Name and Disease are required")
            return False

        result = self.repo.add_doctor(name, disease)

        if result:
            print("Doctor Added Successfully")
        else:
            print("Doctor Insert Failed")

        return result


    # 2. GET ALL DOCTORS
    def get_all_doctors(self):

        doctors = self.repo.get_all_doctors()

        for doctor in doctors:
            print(
                "ID:", doctor[0],
                "Name:", doctor[1],
                "Disease:", doctor[2]
            )

        return doctors


    # 3. GET DOCTOR BY ID
    def get_doctor_by_id(self, doctor_id):

        doctors = self.repo.get_all_doctors()

        for doctor in doctors:

            if doctor[0] == doctor_id:
                print("Doctor Found")
                return doctor

        print("Doctor Not Found")
        return None


    # 4. UPDATE DOCTOR
    def update_doctor(self, doctor_id, name, disease):

        if not name or not disease:
            print("Name and Disease are required")
            return False

        result = self.repo.update_doctor(
            doctor_id, name, disease
        )

        if result:
            print("Doctor Updated Successfully")
        else:
            print("Doctor Not Found")

        return result


    # 5. DELETE DOCTOR
    def delete_doctor(self, doctor_id):

        result = self.repo.delete_doctor(doctor_id)

        if result:
            print("Doctor Deleted Successfully")
        else:
            print("Doctor Not Found")

        return result

