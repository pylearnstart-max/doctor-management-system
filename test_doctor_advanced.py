from service import DoctorService

service = DoctorService()

# 1. SEARCH BY NAME
print("SEARCH BY NAME")

doctors = service.search_doctor_by_name("Ravi")

for doctor in doctors:
    print(doctor)


# 2. SEARCH BY DISEASE
print("\nSEARCH BY DISEASE")

doctors = service.search_doctor_by_disease("Fever")

for doctor in doctors:
    print(doctor)


# 3. TOTAL DOCTOR COUNT
print("\nTOTAL DOCTORS")

print(service.get_doctor_count())