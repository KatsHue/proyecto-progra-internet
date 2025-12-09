<div align="center">

<h2 align="center">✍️ Better | Essay (Mejorado) </h2>

Aplicación web que **corrige ensayos y genera resúmenes** automáticamente utilizando modelos de **Inteligencia Artificial**.  
Desarrollada con **React + Node.js + Express + MongoDB Atlas + FastAPI**, e integrada con **OpenRouter (GPT-4o-mini)** y **Hugging Face (facebook/mbart-large-50, usado en lugar de DistilBART debido a su mayor capacidad multilingüe y mejor rendimiento en textos largos).**.

> 💡 Asegúrate de abrir primero el backend y esperar a que cargue para iniciar sesión correctamente: <br>
> **Puedes usar este usuario y contraseña si no deseas registrarte:**<br>
> **usuario: correo@gmail.com | contraseña: password**

> 💡 Error de registro de usuarios nuevos arreglado <br>

<br>

<a href="https://proyecto-backend-betteressay.onrender.com" target="_blank"><strong>⚙️ Backend</strong></a>  
<a href="https://proyecto-better-essay.onrender.com" target="_blank"><strong>💻 Demo</strong></a> <br>
<a href="https://www.canva.com/design/DAG6rEeO8Z4/ZklRofuhZL_9mmEs9fwRbw/edit?utm_content=DAG6rEeO8Z4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton" target="_blank"><strong>📊 Presentación</strong></a>  

<br><br>
📚 <strong>Programación para Internet 2025B</strong>
</div>

---

## 🚀 Descripción del Proyecto

**Better Essay**:
- Corrige ensayos de forma automática, detectando errores gramaticales, de estilo y coherencia.
- Reescribe el texto de manera clara y profesional.
- Genera resúmenes precisos de textos extensos.

---

## 🧩 Arquitectura del Sistema

```plaintext
Frontend (React)
   ↓
Backend (Node.js + Express)
   ↓
MongoDB Atlas (Base de datos)
   ↓
Servicios IA:
   ├── OpenRouter (GPT-4o-mini) → Corrección de ensayos
   └── Hugging Face (mBART) → Generación de resúmenes
```

## Capturas

<img width="400" alt="image" src="https://github.com/user-attachments/assets/57c9c9d4-e723-4175-8168-394b3a8b4f2c" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/be1739a4-4a08-4511-8395-456d0dfd4351" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/aea7371e-bb81-408b-97be-36a7f4c1ff1c" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/8bdaf38c-c9f3-43e5-bee9-43017fa3f082" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/4b322f89-cdc5-4698-a48e-c4c86b815f7d" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/bca28b71-b059-4013-86b1-98e23920bd6d" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/47eec8a8-bc2c-47cc-86f4-35daa3076582" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/dbe8f087-5861-4219-bb3b-4fe95dd05cc6" />


## Instalación y uso

## Backend
### Clona el repositorio

```sh
git clone https://github.com/KatsHue/proyecto-progra-internet.git
```

### Entra a la carpeta del backend

```sh
cd proyecto-progra-internet
cd backend
```

### Instala dependencias

```sh
npm install
```

### Crear archivo .env dentro de la carpeta backend con las siguientes variables:

```sh
DATABASE_URL = tu_uri_de_mongodb_atlas_aqui (Debes crear una base de datos para los usuarios y su contraseña)

FRONTEND_URL=http://localhost:5173

(sendgrid)
SENDGRID_API_KEY=tu_clave_de_aplicacion_sendgrid
EMAIL_FROM=tu_correo_activado_en_sendgrid

JWT_SECRET=tu_clave_secreta_aqui
```

### Ejecuta el servidor

```sh
npm run dev:api
```

## Frontend
### Entra a la carpeta del frontend 

```sh
cd frontend
```

### Instala dependencias

```sh
npm install
```

### Crear archivo .env.local dentro de la carpeta frontend con las siguientes variables:

```sh
VITE_API_URL= http://localhost:4000/api

VITE_API_IA_KEY=tu_key_de_open_router

VITE_SUMMARY_API=http://127.0.0.1:8000 
```

### Ejecuta el servidor

```sh
npm run dev
```

## IA - Resúmenes
### Entra a la carpeta del ia

```sh
cd ia
```

### Crea un entorno virtual

```sh
python -m venv venv
source venv/Scripts/activate
```

### Instala dependencias

```sh
pip install -r requirements.txt
```

### Ejecuta el servidor

```sh
uvicorn main:app --reload
```

