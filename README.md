### 1. Hola
- **Método:** GET
- **URL:** `/estudiantes/api/v1/hola`
- **Descripción:** Muestra un mensaje genérico de bienvenida.
- **Respuesta:** hola mundo

### 2. Saludo
- **Método:** GET
- **URL:** `/estudiantes/api/v1/saludo`
- **Descripción:** Saluda al estudiante con su nombre.
- **Body (JSON):**
```json
{
  "nombre": "Leonardo",
  "apellido": "Da vinci"


Práctica 3

{
  "mensaje": "Lista de estudiantes obtenida correctamente.",
  "estudiantes": [
    "Ana",
    "Carlos",
    "María"
  ]
}

Agregar un estudiante

{
  "nombre": "Pedro"
}

Respuesta

{
  "mensaje": "Estudiante agregado correctamente.",
  "estudiante": "Pedro"
}

Actualizar un estudiante

{
  "nombre": "Pedro Ramírez"
}
Respuesta

{
  "mensaje": "Estudiante actualizado correctamente.",
  "id": 1
}

Eliminar un estudiante

{
  "mensaje": "Estudiante eliminado correctamente.",
  "id": 1
}
