# Informática Industrial

Repositorio con las presentaciones de la asignatura de Informática Industrial y Comunicaciones.

Este proyecto contiene diapositivas en HTML utilizando Reveal.js, así como recursos visuales y materiales docentes para apoyar la impartición de la asignatura.

## Contenido

- `index.html`: página principal de acceso a la presentación.
- `temas/`: diapositivas del curso, incluyendo la presentación del tema 0.
- `css/`: estilos personalizados del tema visual.
- `assets/`: recursos gráficos y logotipos.

## Uso

Puedes abrir `index.html` en un navegador para visualizar la presentación.

### Exportar una presentación a PDF

Con Python instalado, ejecuta desde la carpeta del repositorio:

```powershell
py -m pip install -r requirements.txt
py -m playwright install chromium
py exportar_pdf_comunicaciones.py
```

El PDF se guarda en `temas/comunicaciones/comunicaciones.pdf`.

## Objetivo

Servir como material docente para la asignatura de Informática Industrial y Comunicaciones, con presentaciones estructuradas y fáciles de reutilizar.
