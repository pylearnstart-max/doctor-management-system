from model import Doctor

doctor1 = Doctor(101, "Ravi", "Fever")
doctor2 = Doctor(102, "Sita", "Diabetes")

print("Doctor 1")
print(doctor1.doctor_id)
print(doctor1.name)
print(doctor1.disease)

print("Doctor 2")
print(doctor2.doctor_id)
print(doctor2.name)
print(doctor2.disease)