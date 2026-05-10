# Calculadora web

La interfaz visual está en `index.html` (raíz del repo) para que también se pueda publicar fácil en GitHub Pages.

## Verla localmente

```bash
python3 -m http.server 8000
```

Abrir en navegador:

- `http://localhost:8000/`

## Verla desde GitHub (interfaz, no solo código)

1. En GitHub entra a **Settings → Pages**.
2. En **Build and deployment**, selecciona:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main` (o la rama principal) y carpeta `/ (root)`
3. Guarda los cambios y espera el deploy.
4. GitHub mostrará la URL pública, por ejemplo:
   - `https://TU_USUARIO.github.io/TU_REPO/`

## Operaciones soportadas

- Suma (`+`)
- Resta (`-`)
- Multiplicación (`*`)
- División (`/`) con validación de división por cero.
