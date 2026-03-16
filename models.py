from sqlalchemy import Column, Integer, String, DECIMAL, Text
from database import Base  # Base de SQLAlchemy para crear las tablas

class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    categoria = Column(String(50))
    cantidad = Column(Integer, nullable=False)
    valor_unitario = Column(DECIMAL(10,2))
    id_proveedor = Column(Integer)

class Proveedor(Base):
    __tablename__ = "proveedores"
    id_proveedor = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20))
    email = Column(String(100))
    direccion = Column(String(150))

class Empleado(Base):
    __tablename__ = "empleados"
    id_empleado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    cargo = Column(String(50))
    email = Column(String(100))

class Categoria(Base):
    __tablename__ = "categorias"
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)

class Ubicacion(Base):
    __tablename__ = "ubicaciones"
    id_ubicacion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    direccion = Column(String(150))