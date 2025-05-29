from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import get_db, Patient, Doctor, Appointment, Prescription
from schemas import PatientSchema, DoctorSchema, PrescriptionSchema, AppointmentSchema

# initialization
app = FastAPI()

# network requests from all servers
app.add_middleware(CORSMiddleware, allow_origins=["*"])


# gets all patients
@app.get("/patients")
def patients(session: Session = Depends(get_db)):
    patients = session.query(Patient).all()
    return patients


# adding a patient
@app.post("/patients")
def add_patient(patient: PatientSchema, db: Session = Depends(get_db)):
    new_patient = Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return {"message": "Patient added successfully"}


# gets all doctors
@app.get("/doctors")
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()


# adding a doctor
@app.post
def add_doctor(doctor: DoctorSchema, db: Session = Depends(get_db)):
    new_doctor = Doctor(**doctor.model_dump())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor


# gets all appointments
@app.get("/appointments")
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()


# adding an appointment
@app.post("/appointments")
def add_appointment(appointment: AppointmentSchema, db: Session = Depends(get_db)):
    new_appointment = Appointment(**appointment.model_dump())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

# gets all prescriptions 
app.get("/prescriptions")
def get_prescriptions(db: Session = Depends(get_db)):
    return db.query(Prescription).all()

# adding a prescription
@app.post("/prescriptions")
def add_prescription(prescription: PrescriptionSchema, db: Session = Depends(get_db)):
    new_prescription = Prescription(**prescription.model_dump())
    db.add(new_prescription)
    db.commit()
    db.refresh(new_prescription)
    return new_prescription