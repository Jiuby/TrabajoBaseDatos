## ⚙️ Pasos para ejecutar el proyecto localmente

### 1. Clona el repositorio y ejecute los siguientes comandos

```bash
git clone https://github.com/Jiuby/TrabajoBaseDatos.git
cd TrabajoBaseDatos
```
```python
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

para crear un usuario admin es desde
```python
python manage.py createsuperuser
```
luego se mete a 
http://127.0.0.1:8000/admin
