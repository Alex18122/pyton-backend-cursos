# API REST: interfaz de programacion de aplicaciones para compartir recursos

from typing import List, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inicializamos una variable donde tendra todas las caracteristicas de una API REST
app = FastAPI()

#Aca definimos el modelo
class Curso(BaseModel):
    id: str
    nombre: str
    descripcion: Optional[str] = None 
    nivel: str
    duracion: int

# Simularemos una base de datos
cursos_db = []

# CRUD: Read(Lectura) GET ALL: Leeremos todos los cursos que haya en la db

@app.get("/cursos", response_model=List[Curso])
def obtener_cursos():
    return cursos_db

# CRUD: Create(Crear/Escribir) POST: agregaremos un nuveo recurso a nuestra base de datos
@app.post("/cursos", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4()) # Usamos uuid para generar un id unico e irrepetible
    cursos_db.append(curso) 

# CRUD: Read(Lectura) GET(individual): Leeremos el curso que coincida con el ID que pidamos
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None) # Con next tomamos la primera coincidencia del array devuelto
    if curso is None:
        raise HTTPException(status_code=404, detail = "Curso no encontrado")
    return curso

# CRUD: Update (Actualizar/Modificar) PUT: modificaremos un recurso que coincida con el ID que mandemos
@app.get("/cursos/{curso_id}", response_model= Curso)
def modificar_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id) , None)
    if curso is None:
        raise HTTPException(status_code=404, detail = "curso no encontrado")
    return curso

