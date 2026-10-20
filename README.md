# API Estudiantes - Práctica de Endpoints

API sencilla creada con Flask para la práctica de endpoints.

## Endpoints

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
}
