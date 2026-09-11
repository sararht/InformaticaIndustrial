import os
import asyncio
from playwright.async_api import async_playwright

async def exportar_presentacion_pdf():
    # 1. Definir rutas relativas/absolutas del proyecto
    rel_html_path = os.path.join("temas", "programacionC", "tema-01-computadoryC.html")
    rel_pdf_path = os.path.join("temas", "programacionC", "tema-01-computadoryC.pdf")
    
    abs_html_path = os.path.abspath(rel_html_path)
    abs_pdf_path = os.path.abspath(rel_pdf_path)

    # Verificar existencia del HTML
    if not os.path.exists(abs_html_path):
        print(f"❌ ERROR: No se encontró el archivo HTML en: {abs_html_path}")
        return

    # URL local con parámetro de impresión nativo de Reveal.js
    file_url = f"file://{abs_html_path}?print-pdf"

    async with async_playwright() as p:
        print("🚀 Iniciando navegador en segundo plano...")
        # Lanza Chromium local
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2  # Mayor nitidez tipográfica en PDF
        )
        page = await context.new_page()

        print(f"📄 Cargando presentación y hoja CSS (`css/uniovi-theme.css`):")
        print(f"   {file_url}")
        
        await page.goto(file_url, wait_until="networkidle")

        # Tiempo de espera para la renderización de Reveal.js, Highlight.js y math.h
        await asyncio.sleep(2.5)

        print("🖨️  Generando PDF con gráficos de fondo y CSS cargado...")
        await page.pdf(
            path=abs_pdf_path,
            format="A4",
            landscape=True,
            print_background=True,  # OBLIGATORIO: Conserva los colores de uniovi-theme.css
            margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
        )

        await browser.close()
        print(f"\n✅ ¡PDF exportado exitosamente!")
        print(f"📍 Ubicación: {abs_pdf_path}")

if __name__ == "__main__":
    asyncio.run(exportar_presentacion_pdf())