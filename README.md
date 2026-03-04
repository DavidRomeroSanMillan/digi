# Digi — Gestión de Hotel

Una aplicación web Django para gestionar clientes, habitaciones e ítems de un hotel. Permite crear, editar, eliminar y visualizar información de clientes, habitaciones y sus ocupantes.

## Tabla de contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Primeros pasos](#primeros-pasos)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Solución de problemas](#solución-de-problemas)

## Requisitos

- Python 3.8 o superior
- Git (para clonar el repositorio)
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/DavidRomeroSanMillan/digi.git
cd digi
```

### 2. Crear y activar un entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
# Si PowerShell bloquea scripts, ejecuta primero:
# powershell -ExecutionPolicy Bypass -NoProfile -Command ". .\venv\Scripts\Activate.ps1"
```

**Windows (CMD):**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

Asegúrate de estar en la carpeta raíz del proyecto (donde están los archivos `manage.py` y `requirements.txt`):

```bash
cd C:\Users\TuUsuario\Desktop\digi
```

Luego instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

Si ves un error "Could not open requirements file", significa que no estás en el directorio correcto. Verifica con:

```bash
dir requirements.txt
```

### 4. Configurar la base de datos

```bash
python manage.py migrate
```

### 5. Crear un superusuario (administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla. Te pedirá:
- Nombre de usuario
- Email
- Contraseña (dos veces)

### 6. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## Primeros pasos

1. **Acceder al panel de administración:**
   - Ve a `http://127.0.0.1:8000/admin/`
   - Inicia sesión con el superusuario creado

2. **Crear datos:**
   - En el panel admin puedes crear Clientes, Habitaciones e Items
   - Los clientes pueden ser asignados a habitaciones

3. **Ver la aplicación principal:**
   - Ve a `http://127.0.0.1:8000/core/` para acceder a las vistas principales

## Uso

### Modelos disponibles

**Cliente:**
- Nombre y apellido
- Email (opcional)
- Teléfono (opcional)
- Se puede asignar a una o más habitaciones

**Habitación:**
- Número único
- Cantidad de camas
- Descripción (opcional)
- Puede tener múltiples ocupantes (clientes)

**Item:**
- Nombre
- Descripción (opcional)
- Fecha de creación automática

### Funcionalidades

- Listar clientes, habitaciones e items
- Ver detalles de cada elemento
- Crear nuevos clientes, habitaciones e items
- Editar información existente
- Eliminar clientes, habitaciones e items
- Asignar clientes a habitaciones

## Estructura del proyecto

```
digi/
├── core/                      # Aplicación principal
│   ├── models.py             # Definición de modelos (Cliente, Habitación, Item)
│   ├── views.py              # Vistas de la aplicación
│   ├── urls.py               # Rutas de URLs
│   ├── admin.py              # Configuración del panel admin
│   └── migrations/           # Migraciones de base de datos
├── digi/                      # Configuración del proyecto
│   ├── settings.py           # Configuración de Django
│   ├── urls.py               # URLs principales
│   ├── wsgi.py               # Configuración para producción
│   └── asgi.py               # Configuración para ASGI
├── templates/                # Plantillas HTML
│   ├── base.html             # Plantilla base
│   └── core/                 # Plantillas de la app core
├── db.sqlite3                # Base de datos (se crea automáticamente)
├── manage.py                 # Script de gestión de Django
└── requirements.txt          # Dependencias del proyecto
```

## Solución de problemas

### PowerShell bloquea la activación del entorno virtual

Si ves un error como "no se puede cargar el archivo", ejecuta:

```powershell
powershell -ExecutionPolicy Bypass -NoProfile -Command ". .\venv\Scripts\Activate.ps1"
```

### Error: "ModuleNotFoundError: No module named 'django'"

Asegúrate de que el entorno virtual está activado y ejecuta:

```bash
pip install -r requirements.txt
```

### Error: "No such table" en la base de datos

Ejecuta las migraciones:

```bash
python manage.py migrate
```

### El servidor no inicia

- Verifica que el puerto 8000 no esté siendo usado por otra aplicación
- Para usar otro puerto: `python manage.py runserver 8001`

### ¿No ves los estilos CSS?

Asegúrate de ejecutar:

```bash
python manage.py collectstatic
```

(Nota: En desarrollo normalmente no es necesario)

## Notas de seguridad

⚠️ **Para desarrollo local solamente:**
- `DEBUG = True` está habilitado en settings.py
- `SECRET_KEY` es insegura
- La base de datos es SQLite (solo para desarrollo)

**Para producción:**
- Cambia `DEBUG = False`
- Genera una `SECRET_KEY` segura
- Usa una base de datos como PostgreSQL
- Configura `ALLOWED_HOSTS` correctamente
- Configura variables de entorno para datos sensibles

---

¿Preguntas o problemas? Revisa la [documentación de Django](https://docs.djangoproject.com/)


