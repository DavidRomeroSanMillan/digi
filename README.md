# Digi — Hotel simple (clientes y habitaciones)

Instrucciones rápidas para clonar y ejecutar este proyecto Django en otro equipo.

Requisitos
- Python 3.8+

Pasos

1) Clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>
```

2) Crear y activar un entorno virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# si PowerShell bloquea: powershell -ExecutionPolicy Bypass -NoProfile -Command ". .venv\\Scripts\\Activate.ps1"
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3) Instalar dependencias

```bash
pip install -r requirements.txt
```


4) Migraciones y base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

5) Crear superusuario (para `admin`)

```bash
python manage.py createsuperuser
```

6) Arrancar servidor

```bash
python manage.py runserver
```


