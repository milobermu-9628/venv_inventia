from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter()

# GET todos los proveedores
@router.get("/", response_model=list[schemas.Proveedor])
def obtener_proveedores(db: Session = Depends(get_db)):
    return db.query(models.Proveedor).all()

# GET proveedor por ID
@router.get("/{id_proveedor}", response_model=schemas.Proveedor)
def obtener_proveedor(id_proveedor: int, db: Session = Depends(get_db)):
    proveedor = db.query(models.Proveedor).filter(models.Proveedor.id_proveedor == id_proveedor).first()
    if not proveedor:
        raise HTTPException(status_code=404, detail=f"Proveedor con id {id_proveedor} no encontrado")
    return proveedor

# POST crear proveedor
@router.post("/", response_model=schemas.Proveedor)
def crear_proveedor(proveedor: schemas.ProveedorCreate, db: Session = Depends(get_db)):
    nuevo_proveedor = models.Proveedor(**proveedor.dict())
    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)
    return nuevo_proveedor

# PUT actualizar proveedor
@router.put("/{id_proveedor}", response_model=schemas.Proveedor)
def actualizar_proveedor(id_proveedor: int, datos: schemas.ProveedorUpdate, db: Session = Depends(get_db)):
    proveedor = db.query(models.Proveedor).filter(models.Proveedor.id_proveedor == id_proveedor).first()
    if not proveedor:
        raise HTTPException(status_code=404, detail=f"Proveedor con id {id_proveedor} no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(proveedor, key, value)
    db.commit()
    db.refresh(proveedor)
    return proveedor

# DELETE proveedor
@router.delete("/{id_proveedor}")
def borrar_proveedor(id_proveedor: int, db: Session = Depends(get_db)):
    proveedor = db.query(models.Proveedor).filter(models.Proveedor.id_proveedor == id_proveedor).first()
    if not proveedor:
        raise HTTPException(status_code=404, detail=f"Proveedor con id {id_proveedor} no encontrado")
    db.delete(proveedor)
    db.commit()
    return {"message": f"Proveedor con id {id_proveedor} eliminado correctamente"}
