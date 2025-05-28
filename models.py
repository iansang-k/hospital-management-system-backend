from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, Date, create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# creating an engine to connect to our database
engine = create_engine("sqlite:///hospital.db", echo=True)

# creating a session
Session = sessionmaker(bind=engine)


# creating a method that returns the session
def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()


# creating a base class
Base = declarative_base()


# creating models for our tables
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    date_of_birth = Column(Date)
    gender = Column(Text)
    phone_number = Column(Text(10))
    emergency_contact = Column(Text)
    emergency_phone_number = Column(Text(10))
    bloodtype = Column(Text)
    created_at = Column(DateTime, default=datetime.now)


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    speciality = Column(Text)
    phone_number = Column(Text(10))


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    patient_id = Column(Integer, ForeignKey("patient.id"))


class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True)
    medication = Column(Text)
    dosage = Column(Text)
    date_prescribed = Column(Date)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    patient_id = Column(Integer, ForeignKey("patient.id"))
