
KINGS Barberia & Peluqueria - Proyecto base
==========================================

Estructura:
- backend/: FastAPI app (SQLite by default). Use DATABASE_URL env var for Postgres.
- frontend/: Vite + React minimal UI.

Credenciales iniciales (creadas automaticamente al iniciar backend):
- Admin: username = KingsBarberia, password = Riverplate22
- Barberos creados: Gustavo, Mauro, Alejandro (contraseña por defecto: <usar create_admin para crear usuarios si se desea>)

Cómo ejecutar local (opcional):
1) Backend:
   - Ir a backend/
   - Crear venv: python -m venv venv
   - Activar: venv\Scripts\activate
   - Instalar: pip install -r requirements.txt
   - Ejecutar: uvicorn app.main:app --reload

2) Frontend:
   - Ir a frontend/
   - npm install
   - npm run dev
   - Abrir http://localhost:5173

Despliegue en Render (resumen):
- Subir este repo a GitHub.
- Crear PostgreSQL en Render (si querés producción) y copiar DATABASE_URL.
- Crear Web Service en Render apuntando a backend/, commandos:
  build: pip install -r requirements.txt
  start: uvicorn app.main:app --host 0.0.0.0 --port $PORT
- Crear Static Site en Vercel o Render para frontend. Configurar variable VITE_API_URL con la URL del backend.

Archivos importantes:
- backend/create_admin.py -> script para crear admin si querés una contraseña diferente (usage: python create_admin.py user pass)
- frontend/public/assets/logo-kings.png -> logo usado en UI

