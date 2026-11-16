
from db import get_connection
from appointment_model import Appointment


class AppointmentRepository:

    # 1. ADD APPOINTMENT
    def add_appointment(self, appointment):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            INSERT INTO dbo.Appointments
            (
                patient_id,
                DoctorID,
                appointment_date,
                appointment_time,
                reason,
                status
            )
            OUTPUT INSERTED.appointment_id
            VALUES (?, ?, ?, ?, ?, ?)
            """

            cursor.execute(query, (
                appointment.patient_id,
                appointment.DoctorID,
                appointment.appointment_date,
                appointment.appointment_time,
                appointment.reason,
                appointment.status
            ))

            appointment_id = cursor.fetchone()[0]

            conn.commit()

            return appointment_id

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()

    # 2. GET ALL APPOINTMENTS
    def get_all_appointments(self):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            SELECT
                appointment_id,
                patient_id,
                DoctorID,
                appointment_date,
                appointment_time,
                reason,
                status
            FROM dbo.Appointments
            ORDER BY appointment_id DESC
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            appointments = []

            for row in rows:

                appointment = Appointment(
                    appointment_id=row[0],
                    patient_id=row[1],
                    DoctorID=row[2],
                    appointment_date=row[3],
                    appointment_time=row[4],
                    reason=row[5],
                    status=row[6]
                )

                appointments.append(appointment.to_dict())

            return appointments

        finally:
            cursor.close()
            conn.close()

    # 3. GET APPOINTMENT BY ID
    def get_appointment_by_id(self, appointment_id):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            SELECT
                appointment_id,
                patient_id,
                DoctorID,
                appointment_date,
                appointment_time,
                reason,
                status
            FROM dbo.Appointments
            WHERE appointment_id = ?
            """

            cursor.execute(query, (appointment_id,))

            row = cursor.fetchone()

            if row is None:
                return None

            appointment = Appointment(
                appointment_id=row[0],
                patient_id=row[1],
                DoctorID=row[2],
                appointment_date=row[3],
                appointment_time=row[4],
                reason=row[5],
                status=row[6]
            )

            return appointment.to_dict()

        finally:
            cursor.close()
            conn.close()

    # 4. UPDATE APPOINTMENT
    def update_appointment(self, appointment_id, appointment):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            UPDATE dbo.Appointments
            SET
                patient_id = ?,
                DoctorID = ?,
                appointment_date = ?,
                appointment_time = ?,
                reason = ?,
                status = ?
            WHERE appointment_id = ?
            """

            cursor.execute(query, (
                appointment.patient_id,
                appointment.DoctorID,
                appointment.appointment_date,
                appointment.appointment_time,
                appointment.reason,
                appointment.status,
                appointment_id
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

    # 5. DELETE APPOINTMENT
    def delete_appointment(self, appointment_id):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            query = """
            DELETE FROM dbo.Appointments
            WHERE appointment_id = ?
            """

            cursor.execute(query, (appointment_id,))

            deleted = cursor.rowcount > 0

            conn.commit()

            return deleted

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()
