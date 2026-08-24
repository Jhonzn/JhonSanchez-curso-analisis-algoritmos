# Laboratorio 02 � Configuraci�n del entorno de trabajo

# Configuración del entorno

## Crear el entorno virtual

```powershell
py3 -m venv venv
```

## Activar el entorno virtual

En PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En CMD:

```cmd
venv\Scripts\activate
```

## Instalar las dependencias

```powershell
python -m pip install --upgrade pip
```

## Instalar una nueva librería

```powershell
pip install matplotlib
```

Después de instalar una nueva librería, actualizar `requirements.txt`:

```powershell
pip freeze > requirements.txt
```

## Ejecutar el proyecto

```powershell
python main.py
```

## Desactivar el entorno virtual

```powershell
deactivate
```

## .gitignore

La carpeta `venv/` no debe subirse a GitHub.

```gitignore
venv/
.venv/
__pycache__/
*.pyc
```

