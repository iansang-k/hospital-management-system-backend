from pydantic import BaseModel
from datetime import datetime, date


class PatientSchema(BaseModel):
    name: str
    date_of_birth: date
    gender: str
    phone_number: str
    emergency_contact: str
    emergency_phone_number: str
    bloodtype: str


class DoctorSchema(BaseModel):
    name: str
    speciality: str
    phone_number: str


class AppointmentSchema(BaseModel):
    date_time: datetime
    doctor_id: int
    patient_id: int


class PrescriptionSchema(BaseModel):
    medication: str
    dosage: str
    date_prescribed: date
    doctor_id: int
    patient_id: int
