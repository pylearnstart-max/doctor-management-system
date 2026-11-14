
from service import DoctorService

service = DoctorService()

# 1. INSERT DOCTOR
print("\n--- INSERT DOCTOR ---")
service.add_doctor("Anil", "Fever")

# 2. GET ALL DOCTORS
print("\n--- ALL DOCTORS ---")
service.get_all_doctors()

# 3. UPDATE DOCTOR
# First check the actual Doctor ID in your database.
print("\n--- UPDATE DOCTOR ---")
service.update_doctor(10, "Ravi Kumar", "Cold")

# 4. GET ALL AFTER UPDATE
print("\n--- AFTER UPDATE ---")
service.get_all_doctors()

# 5. DELETE DOCTOR
# This deletes Doctor ID 10.
print("\n--- DELETE DOCTOR ---")
service.delete_doctor(10)

# 6. GET ALL AFTER DELETE
print("\n--- AFTER DELETE ---")
service.get_all_doctors()
