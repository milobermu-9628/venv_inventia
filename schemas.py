from pydantic import BaseModel
from typing import Optional

# PRODUCTOS

class ProductoBase(BaseModel):
    nombre: str
    categoria: str
    cantidad: int
    valor_unitario: float
    id_proveedor: int

class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    categoria: Optional[str] = None
    cantidad: Optional[int] = None
    valor_unitario: Optional[float] = None
    id_proveedor: Optional[int] = None


class Producto(ProductoBase):
    id_producto: int

    class Config:
        from_attributes = True


# EMPLEADOS

class EmpleadoBase(BaseModel):
    nombre: str
    cargo: str
    email: str


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoUpdate(BaseModel):
    nombre: Optional[str] = None
    cargo: Optional[str] = None
    email: Optional[str] = None


class Empleado(EmpleadoBase):
    id_empleado: int

    class Config:
        from_attributes = True


# =========================
# PROVEEDORES
# =========================

class ProveedorBase(BaseModel):
    nombre: str
    telefono: str
    email: str
    direccion: str


class ProveedorCreate(ProveedorBase):
    pass


class ProveedorUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None


class Proveedor(ProveedorBase):
    id_proveedor: int

    class Config:
        from_attributes = True
