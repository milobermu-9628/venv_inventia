from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter()

# GET TODOS LOS PRODUCTOS
@router.get("/", response_model=list[schemas.Producto])
def obtener_productos(db: Session = Depends(get_db)):
    return db.query(models.Producto).all()


# GET PRODUCTO POR ID
@router.get("/{id_producto}", response_model=schemas.Producto)
def obtener_producto(id_producto: int, db: Session = Depends(get_db)):

    producto = db.query(models.Producto).filter(
        models.Producto.id_producto == id_producto
    ).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto


# POST CREAR PRODUCTO
@router.post("/", response_model=schemas.Producto)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):

    nuevo_producto = models.Producto(**producto.dict())

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


# PUT ACTUALIZAR PRODUCTO
@router.put("/{id_producto}", response_model=schemas.Producto)
def actualizar_producto(id_producto: int, datos: schemas.ProductoUpdate, db: Session = Depends(get_db)):

    producto = db.query(models.Producto).filter(
        models.Producto.id_producto == id_producto
    ).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(producto, key, value)

    db.commit()
    db.refresh(producto)

    return producto


# DELETE PRODUCTO
@router.delete("/{id_producto}")
def eliminar_producto(id_producto: int, db: Session = Depends(get_db)):

    producto = db.query(models.Producto).filter(
        models.Producto.id_producto == id_producto
    ).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()

    return {"mensaje": "Producto eliminado"}
