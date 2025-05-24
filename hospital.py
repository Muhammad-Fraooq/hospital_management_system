from abc import ABC ,abstractmethod
import logging

#? ######################################
#? Start Person Class - Base Class
#? #######################################
class Person:
    def __init__(self,name,age, gender): #! define attributes
        self.name = name 
        self.age = age
        self.gender = gender

    def get_details(self):
        print(f'Name: {self.name}\nAge: {self.age}\nGender: {self.gender}')
        logging.info(f'Name: {self.name}\nAge: {self.age}\nGender: {self.gender}')
        

#? #####################################################
#? Start Patient Class and Inheritance from Person Class
#? #####################################################
class Patient(Person):
    def __init__(self, name, age, gender,patient_id,disease):
        super().__init__(name, age, gender) #! Call the parent class constructor
        self.__patient_id = patient_id
        self.disaese = disease

    #? --- Getters and Setters Methods ---
    def get_details(self): #! Overriding - Polymorphism
        print(f'Patient ID: {self.__patient_id}\nName: {self.name}\nDisease: {self.disaese}')
        logging.info(f'Patient ID: {self.__patient_id}\nName: {self.name}\nDisease: {self.disaese}')

    def get_patient_id(self):
        return self.__patient_id
        
#? #####################################################
#? Start Doctor Class and Inheritance from Person Class
#? #####################################################
class Doctor(Person):
    def __init__(self, name, age, gender,doctor_id,specialization):
        super().__init__(name, age, gender) #! Call the parent class constructor
        self.__doctor_id = doctor_id
        self.specialization = specialization

    def get_details(self): #! Overriding - Polymorphism
        print(f'Doctor ID: {self.__doctor_id}\nName: {self.name}\nSpecialization: {self.specialization}')
        logging.info(f'Doctor ID: {self.__doctor_id}\nName: {self.name}\nSpecialization: {self.specialization}')


    def get_doctor_id(self):
        return self.__doctor_id
    
    def get_specialization(self):
        return self.specialization

#? ########################
#? Start Appointment Class
#? ########################
class Appointment:
    total = 1
    def __init__(self,date,patient,doctor):
        self.date = date 
        self.patient = patient
        self.doctor = doctor
        self.number = Appointment.total
        Appointment.total += 1

    def get_appointment_details(self):
        print(f"\nAppointment ID: {self.number}\nDate: {self.date}.\nPatient: {self.patient.name}.\nDoctor: {self.doctor.name}.\nSpecialization: {self.doctor.specialization}.")
        logging.info(f"\nAppointment ID: {self.number}\nDate: {self.date}.\nPatient: {self.patient.name}.\nDoctor: {self.doctor.name}.\nSpecialization: {self.doctor.specialization}.")
        
#? ############################################
#? Start Hospital Class and use Abstract Class
#? ############################################

class Hospital(ABC):
    def __init__(self):
        self.patient = []
        self.doctor = []
        self.appointment = []

    @abstractmethod
    def book_appointment(self,date,patient,doctor):
        pass

    @abstractmethod
    def cancel_appointment(self):
        pass
