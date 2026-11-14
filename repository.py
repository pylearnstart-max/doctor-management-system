
from db import get_connection


class DoctorRepository:

    # 1. INSERT DOCTOR
    def add_doctor(self, name, disease):

        con = get_connection()

        if con is None:
            return False

        try:
            cursor = con.cursor()

            cursor.execute(
                "INSERT INTO Doctor (Name, Disease) VALUES (?, ?)",
                (name, disease)
            )

            con.commit()
            return True

        except Exception as e:
            print("Insert Error:", e)
            return False

        finally:
            con.close()

    # 2. GET ALL DOCTORS
    def get_all_doctors(self):

        con = get_connection()

        if con is None:
            return []

        try:
            cursor = con.cursor()

            cursor.execute(
                "SELECT DoctorID, Name, Disease FROM Doctor"
            )

            return cursor.fetchall()

        except Exception as e:
            print("Get Error:", e)
            return []

        finally:
            con.close()

    # 3. GET DOCTOR BY ID
    def get_doctor_by_id(self, doctor_id):

        con = get_connection()

        if con is None:
            return None

        try:
            cursor = con.cursor()

            cursor.execute(
                "SELECT DoctorID, Name, Disease FROM Doctor WHERE DoctorID = ?",
                (doctor_id,)
            )

            return cursor.fetchone()

        except Exception as e:
            print("Get Doctor Error:", e)
            return None

        finally:
            con.close()

    # 4. UPDATE DOCTOR
    def update_doctor(self, doctor_id, name, disease):

        con = get_connection()

        if con is None:
            return False

        try:
            cursor = con.cursor()

            cursor.execute(
                "UPDATE Doctor SET Name=?, Disease=? WHERE DoctorID=?",
                (name, disease, doctor_id)
            )

            con.commit()
            return cursor.rowcount > 0

        except Exception as e:
            print("Update Error:", e)
            return False

        finally:
            con.close()

    # 5. DELETE DOCTOR
    def delete_doctor(self, doctor_id):

        con = get_connection()

        if con is None:
            return False

        try:
            cursor = con.cursor()

            cursor.execute(
                "DELETE FROM Doctor WHERE DoctorID=?",
                (doctor_id,)
            )

            con.commit()
            return cursor.rowcount > 0

        except Exception as e:
            print("Delete Error:", e)
            return False

        finally:
            con.close()
