from fastapi import FastAPI, Depends
from models import get_db, Patient

# from schemas import PatientSchema
from sqlalchemy.orm import Session

# initialization
app = FastAPI()


@app.get("/patients")
def patients(session: Session = Depends(get_db)):
    patients = session.query(Patient).all()
    return patients
