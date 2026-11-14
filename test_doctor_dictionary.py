doctors = [
    {
        "id": 1,
        "name": "Ravi",
        "disease": "Fever"
    },
    {
        "id": 2,
        "name": "Sita",
        "disease": "Diabetes"
    },
    {
        "id": 3,
        "name": "Anil",
        "disease": "Cold"
    }
]


# Display All Doctors
def display_doctors(doctors):

    print("\n----- DOCTOR DETAILS -----")

    for doctor in doctors:
        print("ID:", doctor.get("id"))
        print("Name:", doctor.get("name"))
        print("Disease:", doctor.get("disease"))
        print("----------------")


# Search Doctor by ID
def search_doctor(doctors, doctor_id):

    for doctor in doctors:
        if doctor.get("id") == doctor_id:
            return doctor

    return "Doctor Not Found"


# Search Doctor by Name
def search_doctor_by_name(doctors, doctor_name):

    for doctor in doctors:
        if doctor.get("name").lower() == doctor_name.lower():
            return doctor

    return "Doctor Not Found"


# Main Program

display_doctors(doctors)

# ID Search
result = search_doctor(doctors, 2)
print("\nID Search Result:", result)

# Name Search
result = search_doctor_by_name(doctors, "Sita")
print("\nName Search Result:", result)

# Invalid ID Search
result = search_doctor(doctors, 5)
print("\nInvalid ID Search:", result)

# Invalid Name Search
result = search_doctor_by_name(doctors, "Kiran")
print("\nInvalid Name Search:", result)