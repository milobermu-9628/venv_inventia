from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter()

# GET todos los empleados
@router.get("/", response_model=list[schemas.Empleado])
def obtener_empleados(db: Session = Depends(get_db)):
    return db.query(models.Empleado).all()

# GET empleado por ID
@router.get("/{id_empleado}", response_model=schemas.Empleado)
def obtener_empleado(id_empleado: int, db: Session = Depends(get_db)):
    empleado = db.query(models.Empleado).filter(models.Empleado.id_empleado == id_empleado).first()
    if not empleado:
        raise HTTPException(status_code=404, detail=f"Empleado con id {id_empleado} no encontrado")
    return empleado

# POST nuevo empleado
@router.post("/", response_model=schemas.Empleado)
def crear_empleado(empleado: schemas.EmpleadoCreate, db: Session = Depends(get_db)):
    nuevo_empleado = models.Empleado(**empleado.dict())
    db.add(nuevo_empleado)
    db.commit()
    db.refresh(nuevo_empleado)
    return nuevo_empleado

# PUT actualizar empleado
@router.put("/{id_empleado}", response_model=schemas.Empleado)
def actualizar_empleado(id_empleado: int, datos: schemas.EmpleadoUpdate, db: Session = Depends(get_db)):
    empleado = db.query(models.Empleado).filter(models.Empleado.id_empleado == id_empleado).first()
    if not empleado:
        raise HTTPException(status_code=404, detail=f"Empleado con id {id_empleado} no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(empleado, key, value)
    db.commit()
    db.refresh(empleado)
    return empleado

# DELETE empleado
@router.delete("/{id_empleado}")
def borrar_empleado(id_empleado: int, db: Session = Depends(get_db)):
    empleado = db.query(models.Empleado).filter(models.Empleado.id_empleado == id_empleado).first()
    if not empleado:
        raise HTTPException(status_code=404, detail=f"Empleado con id {id_empleado} no encontrado")
    db.delete(empleado)
    db.commit()
    return {"message": f"Empleado con id {id_empleado} eliminado correctamente"}
