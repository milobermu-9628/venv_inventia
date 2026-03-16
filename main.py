from fastapi import FastAPI 
from database import Base, engine
from routers import productos, proveedores, empleados

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="INVENTIA API", description="API de inventario", version="1.0")

# Incluir routers
app.include_router(productos.router, prefix="/productos", tags=["Productos"])
app.include_router(proveedores.router, prefix="/proveedores", tags=["Proveedores"])
app.include_router(empleados.router, prefix="/empleados", tags=["Empleados"])

@app.get("/")
def root():
    return {"message": "Bienvenido a INVENTIA API"}