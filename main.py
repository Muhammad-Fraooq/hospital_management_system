import os
import logging
from rich import box
from rich.panel import Panel
from rich.console import Console
from hospital import Patient,Doctor
from manager import HospitalManager
from exceptions.exceptions import InvalidAgeError,InvalidGenderError,InvalidDateError
from exceptions.main import validate_gender, validate_doctor_age, validate_patient_age,validate_date

#? ✅ Ensure the 'log' directory exists
os.makedirs('log', exist_ok=True)

#? ✅ Set up basic logging configuration
logging.basicConfig(    
    filename='log/hospital.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#? Initialize the console
console = Console()


#?#############################
#? --- Start Main Function ---
#?#############################

def main():
    hospital = HospitalManager()
    while True:

        print("="*50)
        console.print(Panel.fit(
        "[bold cyan]1.[/] ➕ [green]Add (Patient/Doctor)[/]\n"
        "[bold cyan]2.[/] 📅 [yellow]Book Appointment[/]\n"
        "[bold cyan]3.[/] 📋 [blue]Show All Appointments[/]\n"
        "[bold cyan]4.[/] 🔍 [magenta]Search (Patient/Doctor)[/]\n"
        "[bold cyan]5.[/] ⚙️ [bright_cyan] Settings (Patient/Doctor)[/]\n"
        "[bold cyan]6.[/] ❌ [red]Cancel Appointment[/]\n"
        "[bold cyan]7.[/] 🚪 [bold white]Exit[/]",
        title="🏥 [bold underline magenta]Welcome to the Hospital Management System[/]",
        subtitle="Press a number to continue...",
        box=box.DOUBLE
        ))
        print("="*50)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            while True:
                print("\n1. Add Patient\n2. Add Doctor\n3. Back")

                choice = input("\nEnter your choice: ")

                if choice == "1":
                    name = input("Enter patient name: ").lower().strip()
                    # Input and validate age
                    while True:
                        try:
                            age = int(input("Enter patient age: "))
                            validate_patient_age(age)
                            break
                        except InvalidAgeError as e:
                            print(e)
                            logging.error(e)
                    # Input and validate gender
                    while True:
                            try:
                                gender = input("Enter doctor gender (M/F/O): ")
                                validate_gender(gender)
                                break
                            except InvalidGenderError as e:
                                print(e)
                                logging.error(e)

                    patient_id = int(input("Enter patient ID: "))
                    disease = input("Enter patient disease: ")
                    patient = Patient(name,age,gender,patient_id,disease)
                    for pat in hospital.patient:
                        if pat.get_patient_id() == patient_id:
                            print(f"\nPatient with ID {patient_id} already exists!\n")
                            break
                    else:
                        hospital.add_patient(patient)
                        hospital.save_data()
                        print(f"\nPatient {patient.name} added successfully!\n")
                        logging.info(f"Patient {patient.name} added successfully!")
                elif choice == "2":
                    name = input("Enter doctor name: ").lower().strip()
                    # Input and validate age
                    while True:
                        try:
                            age = int(input("Enter doctor age: "))
                            validate_doctor_age(age)
                            break
                        except InvalidAgeError as e:
                            print(e)
                            logging.error(e)
                    # Input and validate gender
                    while True:
                        try:
                            gender = input("Enter doctor gender (M/F/O): ")
                            validate_gender(gender)
                            break
                        except InvalidGenderError as e:
                            print(e)
                            logging.error(e)

                    doctor_id = int(input("Enter doctor ID: "))    
                    specialization = input("Enter doctor specialization: ")
                    doctor = Doctor(name,age,gender,doctor_id,specialization)
                    is_doctor_id_exists = any(doc.get_doctor_id() == doctor_id for doc in hospital.doctor)
                    is_specialization_exists = any(doc.get_specialization() == specialization for doc in hospital.doctor)
                    if is_doctor_id_exists and is_specialization_exists:
                        print(f"\nDoctor {doctor.name} already exists!\n")
                    elif is_doctor_id_exists or is_specialization_exists:
                        print(f"\nDoctor with ID {doctor_id} or Specialization {specialization} already exists!\n")
                    else:
                        hospital.add_doctor(doctor)
                        hospital.save_data()
                        print(f"\nDoctor {doctor.name} added successfully!\n")
                        logging.info(f"\nDoctor {doctor.name} added successfully!\n")
                elif choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":     
            while True:
                    try:
                        date = input("Enter date: ")
                        validate_date(date)
                        break
                    except InvalidDateError as e:
                        print(e)
                        logging.error(e)    
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: ")) 
            patient = hospital.search_patient_by_id(patient_id)
            doctor = hospital.search_doctor_by_id(doctor_id)
            if patient and doctor:
                hospital.book_appointment(date,patient,doctor)
                hospital.save_data()
                print(f"Appointment booked successfully for {patient.name} with {doctor.name}!")
                logging.info(f"Appointment booked successfully for {patient.name} with {doctor.name}!")
            else:
                print(f"Not found patient {patient_id} or doctor {doctor_id}")
        elif choice == "3":
            hospital.show_all_appointments()
        elif choice == "4":
            while True:
                print("\n1. Search by Patient ID\n2. Search by Doctor ID\n3. Back")
                choice = input("\nEnter your choice: ")
                if choice == "1":
                    patient_id = int(input("Enter patient ID to search: "))
                    patient = hospital.search_patient_by_id(patient_id)
                    if patient != None:
                        patient.get_details()
                    else:
                        print("Patient not found.")
                        logging.warning(f"Patient not found: {patient_id}")
                elif choice == "2":
                    doctor_id = int(input("Enter doctor ID: "))
                    doctor = hospital.search_doctor_by_id(doctor_id)
                    if doctor != None:
                        doctor.get_details()
                    else:
                        print("Doctor not found.")
                        logging.warning(f"Patient not found: {doctor_id}")
                elif choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "5":
            hospital.settings()
            hospital.save_data()
        elif choice == "6":
            try:    
              hospital.cancel_appointment()
              hospital.save_data()
              print("Appointment canceled successfully!")        
            except IndexError:
                print("No appointments found.")
                logging.warning("No appointments found.")
        elif choice == "7":
            print("Thanks for using the Hospital Management System.... Goodbye!")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

#? Run the main function      
if __name__ == "__main__":
    main()