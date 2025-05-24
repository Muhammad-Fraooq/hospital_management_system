import os
import json
import logging
from hospital import Hospital,Patient,Doctor,Appointment
from exceptions.exceptions import InvalidAgeError,InvalidGenderError
from exceptions.main import validate_gender, validate_doctor_age, validate_patient_age

#? #############################################
#? Start HospitalManager Class inheriting from Hospital
#? #############################################

class HospitalManager(Hospital):
    def __init__(self):
        super().__init__()
        os.makedirs("data", exist_ok=True)  # safe for nested folders too
        self.storage_file = os.path.join("data", "hospital-data.json")
        self.load_data()

    def load_data(self):
        try:
            with open(self.storage_file,'r') as f:
                data = json.load(f)

            # load patient
            for p in data.get("patients",[]):
                patient = Patient(p["name"],p["age"],p["gender"],p["id"],p["disease"])
                self.patient.append(patient)

            # load doctor
            for d in data.get("doctors",[]):
                doctor = Doctor(d["name"],d["age"],d["gender"],d["id"],d["specialization"])
                self.doctor.append(doctor)

            # load appointment
            for app in data.get("appointments",[]):
                pat = self.search_patient_by_id(app["patient_id"])
                doc = self.search_doctor_by_id(app["doctor_id"])
                if pat and doc:
                    appointment = Appointment(app["date"],pat,doc)
                    self.appointment.append(appointment)
            
        except (FileNotFoundError,json.JSONDecodeError):
            self.patient = []
            self.doctor = []
            self.appointment = []

    def save_data(self):
        data = {
            "patients": [
                {
                "name": p.name,
                "age": p.age,
                "gender": p.gender,
                "id": p.get_patient_id(),
                "disease": p.disaese
                } for p in self.patient],

            "doctors": [
                {
                "name": d.name,
                "age": d.age,
                "gender": d.gender,
                "id": d.get_doctor_id(),
                "specialization": d.specialization
                } for d in self.doctor],

            "appointments": [
                {
                "date": a.date,
                "patient_id": a.patient.get_patient_id(),
                "doctor_id": a.doctor.get_doctor_id()
                } for a in self.appointment]
        }

        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=4)

    def add_patient(self,patient):
        return self.patient.append(patient)
    
    def add_doctor(self,doctor):
        self.doctor.append(doctor)
    
    def book_appointment(self, date, patient, doctor):
        new_appointment = Appointment(date,patient,doctor)
        new_appointment.patient = patient
        new_appointment.doctor = doctor
        return self.appointment.append(new_appointment)

    def cancel_appointment(self):
        return self.appointment.pop()
    
    def show_all_appointments(self):
        if self.appointment:
            for app in self.appointment:
                app.get_appointment_details()
        else:
            print("No appointments found.")
            logging.warning("No appointments found.")

    def search_patient_by_id(self,patient_id):
        for patient in self.patient:
            if patient.get_patient_id() == patient_id:
                return patient
        return None
    
    def search_doctor_by_id(self,doctor_id):
        for doctor in self.doctor:
            if doctor.get_doctor_id() == doctor_id:
                return doctor
        return None
        
    def settings(self):
        while True:
            print("\n1. Patient\n2. Doctor\n3. Back")
            choice = input("\nEnter your choice : ")
            #? settings patient
            if choice == "1":
                while True:
                    print("\n1. Update\n2. Delete\n3. Back")
                    choice = input("\nEnter your choice: ")

                    if choice == "1":
                        patient_id = int(input("Enter patient ID to update details: "))
                        for patient in self.patient:
                            if patient.get_patient_id() == patient_id:
                                print("Leave the field empty if you don't want to update it.")
                                patient.name = input(f"Enter the new patient name ({patient.name}): ") or patient.name
                                 # Input and validate age
                                while True:
                                    try:
                                        patient.age = int(input(f"Enter the new patient age ({patient.age}): ")) or patient.age
                                        validate_patient_age(patient.age)
                                        break
                                    except InvalidAgeError as e:
                                        print(e)
                                        logging.error(e)
                                # Input and validate gender
                                while True:
                                    try:
                                        patient.gender = input(f"Enter the new patient gender (M/F/O) ({patient.gender}): ") or patient.gender
                                        validate_gender(patient.gender)
                                        break
                                    except InvalidGenderError as e:
                                        print(e)
                                        logging.error(e)
                                patient.disaese = input(f"Enter the new patient disaese ({patient.disaese}): ") or patient.disaese
                                print(f"\nPatient with ID {patient_id} updated successfully!\n")
                                logging.info(f"Patient with ID {patient_id} updated successfully!")
                                self.save_data()
                                break
                            else:
                                print(f"Patient with ID {patient_id} not found!")

                    elif choice == "2":
                        patient_id = int(input("Enter patient ID to delete: "))
                        for patient in self.patient:
                            if patient.get_patient_id() == patient_id:
                                self.patient.remove(patient)
                                print(f"\nPatient with ID {patient_id} deleted successfully!\n")
                                logging.info(f"Patient with ID {patient_id} deleted successfully!")
                                self.save_data()
                                break
                            else:
                                print(f"Patient with ID {patient_id} not found!")
                                logging.warning(f"Patient with ID {patient_id} not found!")
                    elif choice == "3":
                        break
                    else:
                        print("\nInvalid choice please try again!\n")

            #? settings doctor
            elif choice == "2":
                while True:
                    print("\n1. Update\n2. Delete\n3. Back")
                    choice = input("\nEnter your choice: ")

                    if choice == "1":
                        doctor_id = int(input("Enter doctor ID to update details: "))
                        for doctor in self.doctor:
                            if doctor.get_doctor_id() == doctor_id:
                                print("Leave the field empty if you don't want to update it.")
                                doctor.name = input(f"Enter the new doctor name ({doctor.name}): ") or doctor.name
                                # Input and validate age
                                while True:
                                    try:
                                        doctor.age = int(input(f"Enter the new doctor age ({patient.age}): ")) or doctor.age
                                        validate_doctor_age(doctor.age)
                                        break
                                    except InvalidAgeError as e:
                                        print(e)
                                        logging.error(e)
                                # Input and validate gender
                                while True:
                                    try:
                                        doctor.gender = input(f"Enter the new doctor gender (M/F/O) ({doctor.gender}): ") or doctor.gender
                                        validate_gender(doctor.gender)
                                        break
                                    except InvalidGenderError as e:
                                        print(e)
                                        logging.error(e)
                                doctor.specialization = input(f"Enter the new doctor specialization ({doctor.specialization}): ") or doctor.specialization
                                print(f"\nDoctor with ID {doctor_id} updated successfully!\n")
                                logging.info(f"Doctor with ID {doctor_id} updated successfully!")
                                self.save_data()
                                break
                            else:
                                print(f"Doctor with ID {doctor_id} not found!")
                    elif choice == "2":
                        doctor_id = int(input("Enter doctor ID to delete: "))
                        for doctor in self.doctor:
                            if doctor.get_doctor_id() == doctor_id:
                                self.doctor.remove(doctor)
                                print(f"\nDoctor with ID {doctor_id} deleted successfully!\n")
                                logging.info(f"Doctor with ID {doctor_id} deleted successfully!")
                                self.save_data()
                                break
                            else:
                                print(f"Doctor with ID {doctor_id} not found!") 
                                logging.warning(f"Doctor with ID {doctor_id} not found!")
                    elif choice == "3":
                        break
                    else:
                        print("\nInvalid choice please try again!\n")
            elif choice == "3":
                break
            else:
                print("\nInvalid choice please try again!\n")

