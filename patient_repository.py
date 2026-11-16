
from db import get_connection
from patient_model import Patient


class PatientRepository:

    # 1. ADD PATIENT
    def add_patient(self, patient):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            INSERT INTO dbo.Patients
            (
                patient_name,
                age,
                gender,
                phone,
                email,
                address,
                disease
            )
            OUTPUT INSERTED.patient_id
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            cursor.execute(query, (
                patient.patient_name,
                patient.age,
                patient.gender,
                patient.phone,
                patient.email,
                patient.address,
                patient.disease
            ))

            patient_id = cursor.fetchone()[0]

            conn.commit()

            return patient_id

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()

    # 2. GET ALL PATIENTS
    def get_all_patients(self):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            SELECT
                patient_id,
                patient_name,
                age,
                gender,
                phone,
                email,
                address,
                disease
            FROM dbo.Patients
            ORDER BY patient_id
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            patients = []

            for row in rows:

                patient = Patient(
                    patient_id=row[0],
                    patient_name=row[1],
                    age=row[2],
                    gender=row[3],
                    phone=row[4],
                    email=row[5],
                    address=row[6],
                    disease=row[7]
                )

                patients.append(patient.to_dict())

            return patients

        finally:
            cursor.close()
            conn.close()

    # 3. GET PATIENT BY ID
    def get_patient_by_id(self, patient_id):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            SELECT
                patient_id,
                patient_name,
                age,
                gender,
                phone,
                email,
                address,
                disease
            FROM dbo.Patients
            WHERE patient_id = ?
            """

            cursor.execute(query, (patient_id,))

            row = cursor.fetchone()

            if row is None:
                return None

            patient = Patient(
                patient_id=row[0],
                patient_name=row[1],
                age=row[2],
                gender=row[3],
                phone=row[4],
                email=row[5],
                address=row[6],
                disease=row[7]
            )

            return patient.to_dict()

        finally:
            cursor.close()
            conn.close()

    # 4. UPDATE PATIENT
    def update_patient(self, patient_id, patient):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            UPDATE dbo.Patients
            SET
                patient_name = ?,
                age = ?,
                gender = ?,
                phone = ?,
                email = ?,
                address = ?,
                disease = ?
            WHERE patient_id = ?
            """

            cursor.execute(query, (
                patient.patient_name,
                patient.age,
                patient.gender,
                patient.phone,
                patient.email,
                patient.address,
                patient.disease,
                patient_id
            ))

            updated = cursor.rowcount > 0

            conn.commit()

            return updated

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()

    # 5. DELETE PATIENT
    def delete_patient(self, patient_id):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            DELETE FROM dbo.Patients
            WHERE patient_id = ?
            """

            cursor.execute(query, (patient_id,))

            deleted = cursor.rowcount > 0

            conn.commit()

            return deleted

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()
