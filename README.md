
# 🎬 **AppMovies** 🎥

¡Bienvenido a **AppMovies**! Esta es una aplicación moderna y fácil de usar que te permite ver información detallada sobre tus películas favoritas. Con una interfaz interactiva y fluida, podrás explorar los detalles de las películas más populares, incluyendo sinopsis, actores, directores y mucho más.

## 🔧 **Tecnologías** 💻

- **Backend**:  
  - **Python** 🐍  
  - **Django** ⚙️  
  - **Django Rest Framework (DRF)** 📡
  
- **Frontend**:  
  - **Angular 17** 🔥  
  - **Tailwind CSS** 💅 (para un diseño moderno y receptivo)

## 📌 **Características** 🧑‍💻

- **Búsqueda de Películas**: Encuentra películas rápidamente mediante una barra de búsqueda.
- **Detalles completos de la película**: Sinopsis, año de estreno, elenco, director, y más.
- **Interfaz amigable**: Diseño limpio y fácil de usar, con soporte para dispositivos móviles.
- **Datos actualizados**: Información de películas obtenida desde una API interna, la que se actualiza permanentemente.

## 🛠️ **Instalación** 🚀

### Requisitos

- Python 3.8+  
- Node.js 14+  
- npm 6+  
- Django 4.0+  
- Angular 17+

### Backend

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/AppMovies.git
   ```

2. Navega al directorio del backend:
   ```bash
   cd AppMovies/backend
   ```

3. Crea un entorno virtual e instálalo:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   .\venv\Scripts\activate   # Para Windows
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```

6. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```

   El backend estará disponible en `http://127.0.0.1:8000`.

### Frontend

1. Navega al directorio del frontend:
   ```bash
   cd ../frontend
   ```

2. Instala las dependencias de Angular:
   ```bash
   npm install
   ```

3. Ejecuta la aplicación Angular:
   ```bash
   ng serve
   ```

   El frontend estará disponible en `http://localhost:4200`.

### API de Backend

- El backend utiliza **Django Rest Framework** para exponer las rutas API RESTful.
- **Endpoint principal**: `/api/movies/` - Obtén la lista de películas.
- **Endpoint de detalle**: `/api/movies/{id}/` - Obtén los detalles de una película específica.

## 🖼️ **Capturas de Pantalla** 📸

![Captura de Pantalla 1](https://example.com/screenshot1.png)
*Interfaz de búsqueda de películas*

![Captura de Pantalla 2](https://example.com/screenshot2.png)
*Detalles completos de la película*

## 🏁 **¡Listo para explorar las películas!** 🎬

¡Ahora puedes explorar películas y sus detalles de manera fácil y rápida con esta aplicación! Si tienes alguna pregunta, no dudes en abrir un *issue* en GitHub.