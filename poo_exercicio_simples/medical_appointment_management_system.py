#Medical Appointment Management System
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()
class Person: #Pessoa
    def __init__(self, name, age):
        self._name = name #nome
        self._age = age #Idade

class Patient(Person): #👉 Patient inherits from Person
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.appointments = [] # appointments list

    #métodos
    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def __str__(self):
        return f"{self._name} {self._age} ({self.patient_id}, {len(self.appointments)} consulta(s)) "
        

class Doctor(Person): #Doctor inherits from Person
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty #especialidade
        self.appointments = [] # appointments list

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def __str__(self):
        return self._name
class Appointment():
    def __init__(self, patient, doctor, date, reason):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.reason = reason

class Clinic:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    #Methods
    def add_patient(self, patient):
        self.patients.append(patient)
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

        appointment.patient.add_appointment(appointment)
        appointment.doctor.add_appointment(appointment)

    def list_doctor_schedule(self, doctor):
        # print(f"=====  Clinic {self.name}  =====")
        print(f"Dr. {doctor._name}’s Appointments: ")
        for appointment in doctor.appointments:
            print(f"{appointment.date} -> {appointment.patient._name} ({appointment.reason})")
        print()

    def list_patient_history(self, patient):
        print(f"Patient history: {patient._name}")
        for appointment in patient.appointments:
            print(f"{appointment.date} -> {appointment.doctor._name} ({appointment.doctor.specialty})")
        print()

# Creating instances of the class "Patient"
patient1 = Patient('Roberto Santos', 40, 'P0001')
patient2 = Patient('Rafela', 33, 'P0002')
patient3 = Patient('Francisa Silva', 20, 'P0003')
patient4 = Patient('Barbara Escorrega', 16, 'P0004')

# Creating instances of the class "Doctor"

doctor1 = Doctor('Amarildo', 67, 'Cardiology')
doctor2 = Doctor('Pelenilda Sarnenta', 55, 'Dermatology')
doctor3 = Doctor('Beto Barbosa', 80, 'Neurology')

#Creating instances of the class "Clinic"
clinic = Clinic('Health Clinic')

#Add patients to the Clinic class
clinic.add_patient(patient1)
clinic.add_patient(patient2)
clinic.add_patient(patient3)
clinic.add_patient(patient4)

#Add doctors to the Clinic class
clinic.add_doctor(doctor1)
clinic.add_doctor(doctor2)
clinic.add_doctor(doctor3)

#Creating instances of the class Appointment
appointment1 = Appointment(patient1, doctor1, "14/05/2026", "Chest pain")
appointment2 = Appointment(patient2, doctor2, "15/05/2026", "Skin rash")
appointment3 = Appointment(patient3, doctor3, "16/05/2026", "Head pain")
appointment4 = Appointment(patient4, doctor1, "17/05/2026", "Routine exams")

#Adding appoitments to the class Clinic
clinic.add_appointment(appointment1)
clinic.add_appointment(appointment2)
clinic.add_appointment(appointment3)
clinic.add_appointment(appointment4)

#Calling the method list_doctor_schedule Class "Clinic"
clinic.list_doctor_schedule(doctor1)
clinic.list_doctor_schedule(doctor2)
clinic.list_doctor_schedule(doctor3)

#Calling the method list_patient_history Class "Clinic"
clinic.list_patient_history(patient1)
clinic.list_patient_history(patient2)
clinic.list_patient_history(patient3)
clinic.list_patient_history(patient4)




