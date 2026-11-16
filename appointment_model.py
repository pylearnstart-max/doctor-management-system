
class Appointment:

    def __init__(
        self,
        appointment_id=None,
        patient_id=None,
        DoctorID=None,
        appointment_date=None,
        appointment_time=None,
        reason=None,
        status="Scheduled"
    ):

        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.DoctorID = DoctorID
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason
        self.status = status

    def to_dict(self):

        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient_id,
            "DoctorID": self.DoctorID,
            "appointment_date": str(self.appointment_date),
            "appointment_time": str(self.appointment_time),
            "reason": self.reason,
            "status": self.status
        }
