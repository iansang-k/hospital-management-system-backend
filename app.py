from fastapi import FastAPI, Depends, HTTPException
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


# gets a specific patient
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).get(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


# adding a patient
@app.post("/patients")
def add_patient(patient: PatientSchema, db: Session = Depends(get_db)):
    new_patient = Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return {"message": "Patient added successfully"}


# updates a specific patient
@app.patch("/patient/{patient_id}")
def update_patient(
    patient_id: int, patient: PatientSchema, db: Session = Depends(get_db)
):
    db_patient = db.query(Patient).get(patient_id)
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    for key, value in patient.model_dump().items():
        setattr(db_patient, key, value)
    db.commit()
    db.refresh(db_patient)
    return {"message": "Patient record updated successfully"}


# deleting a patient record
@app.delete("/patient/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).get(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(patient)
    db.commit()
    return {"message": "Patient deleted successfully"}


# gets all doctors
@app.get("/doctors")
def get_doctors(session: Session = Depends(get_db)):
    doctors = session.query(Doctor).all()
    return doctors

# gets a specific doctor
@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = db.get(Doctor, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

# adding a doctor
@app.post("/doctors")
def add_doctor(doctor: DoctorSchema, db: Session = Depends(get_db)):
    new_doctor = Doctor(**doctor.model_dump())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return {"message": "Doctor added successfully"}


# updating the record of a specific doctor
@app.patch("/doctors/{doctor_id}")
def update_doctor(doctor_id: int, doctor: DoctorSchema, db: Session = Depends(get_db)):
    db_doctor = db.query(Doctor).get(doctor_id)
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    for key, value in doctor.model_dump().items():
        setattr(db_doctor, key, value)
    db.commit()
    db.refresh(db_doctor)
    return {"message": "Doctor record updated successfully"}


# deleting the record of a specific doctor
@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).get(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    db.delete(doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}


# gets all appointments
@app.get("/appointments")
def get_appointments(session: Session = Depends(get_db)):
    appointments = session.query(Appointment).all()
    return appointments


# getting a specific appointment
@app.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).get(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


# adding an appointment
@app.post("/appointments")
def add_appointment(appointment: AppointmentSchema, db: Session = Depends(get_db)):
    new_appointment = Appointment(**appointment.model_dump())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return {"message": "Appointment created successfully"}


# updating an appointment
@app.patch("/appointments/{appointment_id}")
def update_appointment(
    appointment_id: int, appointment: AppointmentSchema, db: Session = Depends(get_db)
):
    db_appointment = db.query(Appointment).get(appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    for key, value in appointment.model_dump().items():
        setattr(db_appointment, key, value)
    db.commit()
    db.refresh(db_appointment)
    return {"message": "Appointment updated successfully"}


# deleting an appointment
@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).get(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(appointment)
    db.commit()
    return {"message": "Appointment deleted successfully"}


# gets all prescriptions
@app.get("/prescriptions")
def get_prescriptions(session: Session = Depends(get_db)):
    prescriptions = session.query(Prescription).all()
    return prescriptions


# getting a specific prescription
@app.get("/prescriptions/{prescription_id}")
def get_prescription(prescription_id: int, db: Session = Depends(get_db)):
    prescription = db.query(Prescription).get(prescription_id)
    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return prescription


# adding a prescription
@app.post("/prescriptions")
def add_prescription(prescription: PrescriptionSchema, db: Session = Depends(get_db)):
    new_prescription = Prescription(**prescription.model_dump())
    db.add(new_prescription)
    db.commit()
    db.refresh(new_prescription)
    return {"message": "Prescription created successfully"}


# updates a prescription
@app.patch("/prescriptions/{prescription_id}")
def update_prescription(
    prescription_id: int,
    prescription: PrescriptionSchema,
    db: Session = Depends(get_db),
):
    db_prescription = db.query(Prescription).get(prescription_id)
    if not db_prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    for key, value in prescription.model_dump().items():
        setattr(db_prescription, key, value)
    db.commit()
    db.refresh(db_prescription)
    return {"message": "Prescription updated successfully"}


# deletes a prescription
@app.delete("/prescriptions/{prescription_id}")
def delete_prescription(prescription_id: int, db: Session = Depends(get_db)):
    prescription = db.query(Prescription).get(prescription_id)
    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    db.delete(prescription)
    db.commit()
    return {"message": "Prescription deleted successfully"}
