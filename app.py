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

#adding a patient
@app.post("/patients")
def add_patient(patient: PatientSchema, db: Session = Depends(get_db)):
    new_patient = Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return {"message": "Patient added successfully"}

# gets all doctors 
app.get ("/doctors")
def add_doctor(doctor: DoctorSchema, )


